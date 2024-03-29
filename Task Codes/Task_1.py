"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

This is the simple code for path planning class

"""



import math

import matplotlib.pyplot as plt

show_animation = True


class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution # get resolution of the grid
        self.rr = rr # robot radis
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() # motion model for grid search expansion
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y
        

        self.Delta_C1 = 0.2 # cost intensive area 1 modifier
        self.Delta_C2 = 1 # cost intensive area 2 modifier

        self.costPerGrid = 1 


    class Node: # definition of a sinle node
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,open_set[o])) # g(n) and h(n): calculate the distance between the goal node and openset
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',lambda event: [exit(0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                airplane_symbol_5 = "🛩️" #airplane symbol 5
                print()
                print( airplane_symbol_5 + "   Total Trip time required ➜ ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                TotalTime = current.cost

                #For A321neo
                FCR321 = 54 #Fuel Consumption Rate
                PC321 = 200 #Passenger Capacity
                CTL321 = 10 #Cost Time Low
                CTM321 = 15 #Cost Time Medium 
                CTH321 = 20 #Cost Time High
                FC321 = 1800 #Fixed Cost

                #For A330-900neo
                FCR330 = 84 #Fuel Consumption Rate
                PC330 = 300 #Passenger Capacity
                CTL330 = 15 #Cost Time Low
                CTM330 = 21 #Cost Time Medium 
                CTH330 = 27 #Cost Time High
                FC330 = 2000 #Fixed Cost

                #For A350-900
                FCR350 = 90 #Fuel Consumption Rate
                PC350 = 350 #Passenger Capacity
                CTL350 = 20 #Cost Time Low
                CTM350 = 27 #Cost Time Medium 
                CTH350 = 34 #Cost Time High
                FC350 = 2500 #Fixed Cost

                #Setup Scenarios

                #Scenario 1
                TPPW1 = 3000 #Total Passengers Per Week
                MNFPW1 = 12 # Maximum number of flights per week
                FC1 = 0.76 #Fuel Cost

                #Scenario 2
                TPPW2 = 1250 #Total Passengers Per Week
                MNFPW2 = 5 * 20 # Maximum number of flights per week
                FC2 = 0.88 #Fuel Cost

                #Scenario 3
                TPPW3 = 2500 #Total Passengers Per Week
                MNFPW3 = 25 # Maximum number of flights per week
                FC3 = 0.95 #Fuel Cost


                #Scenario 1 
                #Calculate flight numbers
                if TPPW1 % PC321==0:
                    Flight_Number_A321neo_1 = TPPW1 // PC321
                else:
                    Flight_Number_A321neo_1 = TPPW1 // PC321+1

                if TPPW1 % PC330==0:
                    Flight_Number_A330_900neo_1 = TPPW1 // PC330
                else: Flight_Number_A330_900neo_1 = TPPW1 // PC330+1

                if TPPW1 % PC350==0:
                    Flight_Number_A350_900_1 = TPPW1 // PC350
                else: Flight_Number_A350_900_1 = TPPW1 // PC350+1

                #Calculate totol fee
                Cost_A321neo_1 = (FC1 * FCR321 * TotalTime + CTM321 * TotalTime + FC321)*Flight_Number_A321neo_1
                Cost_A330_900neo_1 = (FC1 * FCR330 * TotalTime + CTM330 * TotalTime + FC330)*Flight_Number_A330_900neo_1
                Cost_A350_900_1 = (FC1 * FCR350 * TotalTime + CTM350 * TotalTime + FC350)*Flight_Number_A350_900_1

                #Airplane Symbol
                airplane_symbol = "✈"
                airplane_symbol_2 = "🛫"
                airplane_symbol_3 = "🛬"
                airplane_symbol_4 = "🚁"
                airplane_symbol_5 = "🛩️"
                airplane_symbol_6 = "🛸"

                #Print data
                print("")
                print(" " + airplane_symbol_2 + "  Scenario 1")
                print()

                #A321
                print("    "+ airplane_symbol + "  A321neo")
                if Flight_Number_A321neo_1<MNFPW1:
                    print( str(Flight_Number_A321neo_1) + " flights will complete the task with a total cost of " + str(Cost_A321neo_1))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A321neo_1) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A321neo_1 = 1e9

                #A330
                print()
                print("    "+ airplane_symbol + "  A330-900neo")
                if Flight_Number_A330_900neo_1<MNFPW1:
                    print( str(Flight_Number_A330_900neo_1) + " flights will complete the task with a total cost of " + str(Cost_A330_900neo_1))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A330_900neo_1) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A330_900neo_1 = 1e9
                #A350
                print()    
                print("    "+ airplane_symbol + "  A350-900")
                if Flight_Number_A350_900_1<MNFPW1:
                    print( str(Flight_Number_A350_900_1) + " flights will complete the task with a total cost of " + str(Cost_A350_900_1))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A350_900_1) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A350_900_1 = 1e9
                
                #Find minimum & print
                print()
                print()
                print("    "+ airplane_symbol_3 + "  Result")
                minimum = min(Cost_A321neo_1, Cost_A330_900neo_1, Cost_A350_900_1)
                if minimum == Cost_A321neo_1:
                    print(f'Choosing {Flight_Number_A321neo_1} flights of "A321neo" is the best solution, where the lowest cost is {Cost_A321neo_1}')
                elif minimum == Cost_A330_900neo_1:
                    print(f'Choosing {Flight_Number_A330_900neo_1} flights of "A330-900neo" is the best solution, where the lowest cost is {Cost_A330_900neo_1}')
                elif minimum == Cost_A350_900_1:
                    print(f'Choosing {Flight_Number_A350_900_1} flights of "A350-900" is the best solution, where the lowest cost is {Cost_A350_900_1}')


                #Scenario 2
                #Calculate flight numbers
                if TPPW2 % PC321==0:
                    Flight_Number_A321neo_2 = TPPW2 // PC321
                else:
                    Flight_Number_A321neo_2 = TPPW2 // PC321+1

                if TPPW2 % PC330==0:
                    Flight_Number_A330_900neo_2 = TPPW2 // PC330
                else: Flight_Number_A330_900neo_2 = TPPW2 // PC330+1

                if TPPW2 % PC350==0:
                    Flight_Number_A350_900_2 = TPPW2 // PC350
                else: Flight_Number_A350_900_2 = TPPW2 // PC350+1

                #Calculate totol fee
                Cost_A321neo_2 = (FC2 * FCR321 * TotalTime + CTH321 * TotalTime + FC321)*Flight_Number_A321neo_2
                Cost_A330_900neo_2 = (FC2 * FCR330 * TotalTime + CTH330 * TotalTime + FC330)*Flight_Number_A330_900neo_2
                Cost_A350_900_2 = (FC2 * FCR350 * TotalTime + CTH350 * TotalTime + FC350)*Flight_Number_A350_900_2

                #Print
                print()
                print()
                print("")
                print(" " + airplane_symbol_2 + "  Scenario 2")
                print()

                #A321
                print("    "+ airplane_symbol + "  A321neo")
                if Flight_Number_A321neo_2<MNFPW2:
                    print( str(Flight_Number_A321neo_2) + " flights will complete the task with a total cost of " + str(Cost_A321neo_2))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A321neo_2) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A321neo_2 = 1e9

                #A330
                print()
                print("    "+ airplane_symbol + "  A330-900neo")
                if Flight_Number_A330_900neo_2<MNFPW2:
                    print( str(Flight_Number_A330_900neo_2) + " flights will complete the task with a total cost of " + str(Cost_A330_900neo_2))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A330_900neo_2) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A330_900neo_2 = 1e9

                #A350
                print()    
                print("    "+ airplane_symbol + "  A350-900")
                if Flight_Number_A350_900_2<MNFPW2:
                    print( str(Flight_Number_A350_900_2) + " flights will complete the task with a total cost of " + str(Cost_A350_900_2))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A350_900_2) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A350_900_2 = 1e9
                
                #Find minimum & print
                print()
                print()
                print("    "+ airplane_symbol_3 + "  Result")
                minimum = min(Cost_A321neo_2 , Cost_A330_900neo_2 , Cost_A350_900_2)
                if minimum == Cost_A321neo_2:
                    print(f'Choosing {Flight_Number_A321neo_2} flights of "A321neo" is the best solution, where the lowest cost is {Cost_A321neo_2}')
                elif minimum == Cost_A330_900neo_2:
                    print(f'Choosing {Flight_Number_A330_900neo_2} flights of "A330-900neo" is the best solution, where the lowest cost is {Cost_A330_900neo_2}')
                elif minimum == Cost_A350_900_2:
                    print(f'Choosing {Flight_Number_A350_900_2} flights of "A350-900" is the best solution, where the lowest cost is {Cost_A350_900_2}')
                
                #Scenario 3
                #Calculate flight numbers
                if TPPW3 % PC321==0:
                    Flight_Number_A321neo_3 = TPPW3 // PC321
                else:
                    Flight_Number_A321neo_3 = TPPW3 // PC321+1

                if TPPW3 % PC330==0:
                    Flight_Number_A330_900neo_3 = TPPW3 // PC330
                else: Flight_Number_A330_900neo_3 = TPPW3 // PC330+1

                if TPPW3 % PC350==0:
                    Flight_Number_A350_900_3 = TPPW3 // PC350
                else: Flight_Number_A350_900_3 = TPPW3 // PC350+1

                #Calculate totol fee
                Cost_A321neo_3 = (FC3 * FCR321 * TotalTime + CTL321 * TotalTime + FC321)*Flight_Number_A321neo_3
                Cost_A330_900neo_3 = (FC3 * FCR330 * TotalTime + CTL330 * TotalTime + FC330)*Flight_Number_A330_900neo_3
                Cost_A350_900_3 = (FC3 * FCR350 * TotalTime + CTL350 * TotalTime + FC350)*Flight_Number_A350_900_3

                #Print
                print()
                print()
                print("")
                print(" " + airplane_symbol_2 + "  Scenario 3")
                print()

                #A321
                print("    "+ airplane_symbol + "  A321neo")
                if Flight_Number_A321neo_3<MNFPW3:
                    print( str(Flight_Number_A321neo_3) + " flights will complete the task with total cost of " + str(Cost_A321neo_3))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A321neo_3) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A321neo_3 = 1e9

                #A330
                print()
                print("    "+ airplane_symbol + "  A330-900neo")
                if Flight_Number_A330_900neo_3<MNFPW3:
                    print( str(Flight_Number_A330_900neo_3) + " flights will complete the task with a total cost of " + str(Cost_A330_900neo_3))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A330_900neo_3) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A330_900neo_3 = 1e9

                #A350
                print()      
                print("    "+ airplane_symbol + "  A350-900")
                if Flight_Number_A350_900_3<MNFPW3:
                    print( str(Flight_Number_A350_900_3) + " flights will complete the task with a total cost of " + str(Cost_A350_900_3))
                else:
                    print(""" "NOT VIABLE" , because it requires """ + str(Flight_Number_A350_900_3) + """ flights to complete the task, which exceeds the maximum flight limit.""")
                    Cost_A350_900_3 = 1e9
                               
                #Find minimum & print
                print()
                print()
                print("    "+ airplane_symbol_3 + "  Result")
                minimum = min(Cost_A321neo_3 , Cost_A330_900neo_3 , Cost_A350_900_3)
                if minimum == Cost_A321neo_3:
                    print(f'Choosing {Flight_Number_A321neo_3} flights of "A321neo" is the best solution, where the lowest cost is {Cost_A321neo_3}')
                elif minimum == Cost_A330_900neo_3:
                    print(f'Choosing {Flight_Number_A330_900neo_3} flights of "A330-900neo" is the best solution, where the lowest cost is {Cost_A330_900neo_3}')
                elif minimum == Cost_A350_900_3:
                    print(f'Choosing {Flight_Number_A350_900_3} flights of "A350-900" is the best solution, where the lowest cost is {Cost_A350_900_3}')
                break

                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                ## add more cost in cost intensive area 1
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C1 * self.motion[i][2]
                
                # add more cost in cost intensive area 2
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C2 * self.motion[i][2]
                    # print()
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)] # save the goal node as the first point
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    
    def calc_heuristic_maldis(n1, n2):
        w = 1.0  # weight of heuristic
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x) 

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] # allocate memory
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) # grid position calculation (x,y)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy): # Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
                    d = math.hypot(iox - x, ioy - y) # The math. hypot() method finds the Euclidean norm
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True # the griid is is occupied by the obstacle
                        break

    @staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion


def main():
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # start and goal position
    sx = 50.0  # [m]
    sy = 0.0  # [m]
    gx = 0.0  # [m]
    gy = 50.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    # setting obstacle positions for group 9
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 61): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 61): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    for i in range(-5, 10): # draw the free border
        ox.append(20.0)
        oy.append(i)

    #for i in range(0, 20): # For format reference
        #ox.append(i)
        #oy.append(-1 * i + 10)

    #for i in range(200, 400): #it's not working
    #    ox.append(i/10)
    #    oy.append((1 * i - 200)/10)

    a = 30 #Drawing free border obstacle
    while a <= 35:
        ox.append(a)
        oy.append(-3 * a + 100)
        a = a + 0.3

    b = 20 #Drawing free border obstacle 
    while b <= 40:
        ox.append(b)
        oy.append(b + 20)
        b += 0.7

    # for i in range(40, 45): # draw the button border 
    #     ox.append(i)
    #     oy.append(30.0)


    # set cost intesive area 1
    tc_x, tc_y = [], []
    for i in range(-10, 10):
        for j in range(20, 40):
            tc_x.append(i)
            tc_y.append(j)
    
    # set cost intesive area 2
    fc_x, fc_y = [], []
    for i in range(30, 50):
        for j in range(10, 30):
            fc_x.append(i)
            fc_y.append(j)


    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(sx, sy, "og") # plot the start position 
        plt.plot(gx, gy, "xb") # plot the end position
        
        plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
        plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot


if __name__ == '__main__':
    main()

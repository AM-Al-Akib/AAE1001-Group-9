# AAE1001-Group-9

## Content

* [About Path Planning in Aviation](#about-the-project)
* [Theory of Path Planning Algorithm]
* [Project Video](#Project-Video)
* [Task 1](#task-1)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Task A1](#task-A1)
* [Task A2](#task-A2)
* [Task A3](#task-A3)
* [Usage](#Usage)
* [Reflections](#Reflections)


## About Path Planning in Aviation
Ensuring cost efficiency and passenger satisfaction stands as a pivotal determinant of an airline's success. However, orchestrating a flight from one point to another isn't a straightforward task of just transporting passengers and cargo safely and punctually. The airspace, that expansive canvas of sky above, is essentially claimed by the countries residing beneath it as their territorial domain, often extending up to FL600. Unauthorized entry into this airspace would breach the sovereignty of the respective nation. Thankfully, the Five Freedoms of Air exist to facilitate aviation, though airlines are burdened with charges for traversing foreign airspace.

Beyond diplomatic considerations, the aviation industry grapples with physical obstacles that impact flight paths. These include formidable barriers such as high terrains, ranging from hills to mountains, areas afflicted by adverse weather conditions, and even towering skyscrapers that can impose constraints on an aircraft's mobility during takeoff and landing. 

The crux of this project lies in the pursuit of identifying the most efficient pathway for a flight, navigating through a maze of real-world challenges. Leveraging cutting-edge technologies and methodologies, we aim to optimize flight paths under diverse circumstances, ensuring a harmonious blend of safety, cost-effectiveness, and passenger convenience.


## Theory of Path Planning Algorithm
  Navigating through path planning constitutes a pivotal challenge in robotics research, with its solutions proving instrumental across diverse fields. The application of path planning spans from guiding robots towards specific objectives, involving tasks as straightforward as trajectory planning to the intricacies of selecting a well-suited sequence of actions. The implementation of apt algorithms plays a key role, enabling the broad applicability of path planning in both partially known and unknown structured environments.

Local path planning, a significant facet, involves the generation of paths by assimilating data from sensors while the robot is in motion. This dynamic process empowers the robot to adapt and generate new paths based on real-time environmental data, enhancing its practical utility. In essence, local path planning ensures adaptability in navigating through changing surroundings.

Four paramount trade-off criteria are essential considerations in any path planning algorithm. Optimization, completeness, precision, and execution time stand as key pillars shaping the efficacy of a path planning approach [1]. Striking a balance among these criteria is crucial for developing path planning solutions that are not only effective but also efficient in real-world applications.

## Project Video

[![IMAGE ALT TEXT HERE]()

## Task 1
???

## Task 2
### Goal
To design a new jet stream area which reduce cost by 5%

### Background
The jet stream refers to a narrow and high-altitude air current in the atmosphere, where aircraft will consume less time and fuel whe crusing. It is characterized by high wind speeds and mainly formed due to temperature and pressure differences in the atmosphere. 

![image](https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149348069/2c6b234c-0052-4c29-88b9-1a68ca1a8570)

### Methodology
With the scenario same as Task 1 as the background, we need to find the specific area to set the jet stream where the cost of flight cab reduced by 5%。 The specific area is also required to span across the map laterally and span 5-unit length vertically.

### Coding section

![螢幕截圖 2023-12-02 下午1 56 24](https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149348069/c912c74d-693a-4e57-b7d3-2392c5bc9c80)

This is the part we have added the jet stream area. We have set a range and choose the best area for jet stream base on the best value.

### Results

<img width="1264" alt="螢幕截圖 2023-12-02 下午3 17 03" src="https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149348069/cc6e575d-d303-4d32-ada9-eb8d84fc5eb3">

![螢幕截圖 2023-12-02 下午1 55 32](https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149348069/841aec23-7572-4cfd-abc5-3834415668bf)

For the results, we can conclude that after the use of the jet stream area, the total cost of A330-900 neo is around 85000 usd, while the total cost of A350-900 is around 88300 usd. Futhermore, we can know that A321 neo is not viable in thie scenario.

## Task 3
???

## Task A1
### Goal
1. To add one checkpoint for each cost intensive area(2 in total) 2. To reach all checkpoints before arriving at the destination.

### Background
The primary goal is to deliver essential supplies to two separate locations. These supplies could range from medical and food supplies to technical equipment or humanitarian aid. Precise planning is essential, involving precise calculations for fuel, timing, and the safest and most efficient routes to reach the drop-off points and return to base. The primary mission of the supply craft is the swift and efficient delivery of crucial supplies to two high-priority, cost-intensive areas. Central to this mission is the strategic route planning, which focuses on creating the most direct and practical path between these checkpoints. This optimized routing is key to minimizing travel time and fuel consumption, ensuring the prompt delivery of essential items like medical and food supplies, and technical or humanitarian aid.

### Methodology 
In the given scenario from Task 1, our objective is to refine an existing pathfinding algorithm to automatically incorporate two designated checkpoints within cost-intensive areas. Modify our pathfinding algorithm to include these checkpoints as required waypoints. Once the optimal route is calculated, it should be visualized on the graph. This typically involves plotting the route over a map or graph, with checkpoints and cost-intensive areas clearly marked.

### Coding section
![node.cost](https://cdn.discordapp.com/attachments/901650593637101600/1180256309937963170/Screenshot_2023-12-02_032347.png?ex=657cc258&is=656a4d58&hm=cc2ea909e64dd01faad2074e13848b21cdc2f650c5e333bc11a03f1f0f14a2d2&)

To ensure the A* search algorithm routes the aircraft through the required checkpoints, we modify the 'self.fc_' attribute to represent the x and y coordinates of the two designated checkpoints. By setting the 'node.cost' to zero for these checkpoints, the algorithm is compelled to prioritize these waypoints, effectively guiding the aircraft through these specific locations without adding additional cost to the pathfinding calculation. This strategic adjustment allows the algorithm to seamlessly integrate the required checkpoints into the optimal route.

![plot](https://cdn.discordapp.com/attachments/901650593637101600/1180256309669544148/Screenshot_2023-12-02_032418.png?ex=657cc258&is=656a4d58&hm=76deb31ab3644f67f6e21bdabb1ff073fc6cae677acc6b5b18512a821c78374c&)

At this stage, we will visualize the two checkpoints by marking them in green on the plot.

### Result

![gifv2](https://cdn.discordapp.com/attachments/901650593637101600/1180453332117102603/ezgif.com-video-to-gif.gif?ex=657d79d6&is=656b04d6&hm=aa91b17c198c49150713cf2cf5ca66f828cd572cd2cb770524516eaa91bcf6ea&)

## Task A2
### Goal 

To find the route of minimum cost when obstacles are generated randomly with reasonable density. 

### Background 

Assume the mission and the environment keep changing for each operation. 

1. Only the fuel-consuming area remains and generate it randomly with a fixed area (40x40) 

2. Diagonal movement is disabled, change parameter(s) so that the object could travel within one grid size 

3. Obstacles are generated randomly with reasonable density 

4. Destination and starting points are generated randomly with at least a 40-unit distance in-between 

5. Plotting of the fuel-consuming area would not cover the obstacles, and obstacles should not generate at/near the start and end point 

### Methodology 

In the given scenario from Task 1, the obstacles are fixed and diagonal movement is allowed. But in this task, the diagonal movement is disabled and the obstacles are generated randomly. Therefore, the most challenging part for Additional Task 2 is to modify the code so that the obstacles and the fuel-consuming area can be generated appropriately. Meanwhile, the density of the obstacles must be appropriate. 

### Results 
![pic1]()

![pic2]()

![pic3]()

### Discussion 

If the obstacle density is too high, sometimes the route can not be found because there is no available route for the situation. ChatGPT provides a method to control the density. 

![pic4]()

Sometimes the obstacles may be generated on the position of the start or end nude, which could cause confusion to the code. Thus, the obstacles need to be modified. 

![pic5]()

## Task A3

**Goal**: To test other unalike algorithms for finding the most efficient path.

**Methodology**: We have to choose additional 2 different algorithms from the GitHub platform and compare all 3 codes with outcomes together, with the same obstacle deisgn.

**Result for BFS (sped up by x5)**:

![Untitled ‑ Made with FlexClip (1)](https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149984998/e4f89322-87ac-45bf-8462-194caa6808cc)


Without a doubt, BFS planning requires a considerably longer time compared to A planning. The process of calculating and determining the optimal pathway from the starting point to the destination takes a substantial amount of time. We have even enhanced the speed by a factor of 5 on our GitHub. However, when comparing these two programs, we highly recommend utilizing A path planning as it significantly reduces the time required.

**Results for Dijkstra (sped up by x5)**:

![Untitled ‑ Made with FlexClip (4)](https://github.com/AM-Al-Akib/AAE1001-Group-9/assets/149984998/e7d8e49a-0e90-4daa-92ee-018953bf76fb)


After examining the outcomes of two different coding approaches, it can be concluded that Dijkstra's algorithm finds longer flight paths for the aircraft compared to A path planning, but it is significantly faster than BFS. Even with a 5x speed improvement, Dijkstra's algorithm still takes considerable time due to its extensive path searching. On the other hand, BFS, despite being sped up by 5x, requires even more time for calculations and finding the final path. Therefore, it is evident that A* path planning is the optimal choice for our project. It efficiently reaches the goal point in the shortest possible manner. Hence, selecting A* path planning was the most suitable decision for our coding project.

## Reflection


**AL AKIB Ahmad Munjir's Reflection:** The path planning project was a real rollercoaster, especially given my role as the group leader. Initially, the whole coding seemed like a daunting task, especially since my teammates had no experience in coding, and I did not have any prior experience with path planning. However, leading the group required more than coding skills; it demanded effective management to ensure we did not crash and burn.

Being the leader meant more than just keeping an eye on coding tasks. It meant understanding the strengths and weaknesses of each team member and dishing out responsibilities accordingly. Real talk – not everyone was a coding whiz, so I played smart while coding by getting help from AIs when I couldn’t understand the format or logic behind something. This made coding less of a nightmare.

While leading my group, project management became my new best friend. Organizing the team, setting targets, and throwing deadlines on the table became necessary. Though I couldn't start the project as planned because of a lack of communication issues with my group mates, I was fortunate to start and finish before the deadline. Breaking down the GitHub project into smaller tasks for the team was my way of making sure everyone could chip in.

While the main focus was on coding, the project took us into the nitty-gritty of aviation knowledge and industry terms. Embracing the idea of continuous learning, I dove headfirst into challenges, gaining a deeper understanding of Python coding and the complexities of aviation path planning.

Choosing to work with existing code and a bit of project juggling turned what could have been a coding nightmare into a collaborative learning adventure. It wasn't just about meeting coding requirements; it was about appreciating the intricacies of aviation path planning.

To sum it up, the path planning project was a wild ride that taught me more than just coding. After the experience of leading this group, it was not like just a walk in the garden. Instead, I had to handle many things that were not meant to be initially dealt by me. Still, as mentioned before, my teammates had no coding experience, so I had to do many things while keeping in mind the deadline, but after all, I'm thankful for the team's support and contributions. Together, we ticked off the project's goals, and I tried to maintain a positive learning space.

I look forward to having more learning experiences like this path-planning project in the future.
Then, I hope I’ll be able to reflect on what I learned here. And in this way, I want to increase my understanding of the nitty-gritty of aviation knowledge and industry terms.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**LongYiqi's Reflection:**
It is a pretty surprise for me after heard the requirement from the professor. As a mainland student who just come less than half a year, the coding program is totally a strange area for me, as there is not any course that related to the python. Luckily, it is not necessary for us to do the entire coding, but just adjust some part in the text that professor given to us. After the group discussion, I realize that a complete rookie in coding can done this task if he is willing to learn few by himself. After changed some values and it run perfectly, I was so delighted at the time I successfully run the code. I also find coding is so interesting therefore spending some time to do research. As I am doing additional task 3 coding, it improved my technical skills and make me have more confidence on it. I really enjoy the group working and proud to be a member of this group. After this mission, I realized that coding is also an important and effective tool in aviation industry. I am appreciating to the experience in this group project and other group mates in this group, without them, I cannot done this task, gain more knowledge and meet more friends.--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**'s Reflection:**
=======
**Leung Siu Kwan's Reflection:** The objective of my assignment is to develop an add-on for the code created in Task 1, presenting a blend of straightforward tasks and engaging challenges. The simplicity lies in the foundation provided by the pre-existing code, which spares me from starting from scratch and allows me to focus on modifying and enhancing specific sections. Conversely, the complexity emerges from the necessity to meticulously review and comprehend the original code to determine the precise areas that require adjustments. The analytical process of dissecting the entire codebase is intellectually gratifying, especially when I achieve a thorough understanding of its mechanics and successfully integrate my contributions.
Additionally, contributing to the GitHub README has been an enjoyable aspect of the project. There's a certain pleasure in committing incremental changes and observing the evolution of the document over time. Witnessing the culmination of these small, yet significant, contributions into a comprehensive final product is immensely satisfying. This experience not only enhances my technical skills but also provides a sense of accomplishment in the collaborative and iterative nature of coding.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Chik Long Tin's Reflection:**  I was both surprised and concerned when I realized that coding was necessary for this project. Despite having no prior experience and never anticipating the need to code after high school,  I was assigned to finish Task 2 after discussing with my teammates. Task 2 involved creating a jet stream area with a 5% cost reduction. While I initially thought I would have to write the code from scratch, I soon realized that I only needed to make modifications from the code already existing. However, when I started working on it, I found myself, without no surprise, struggling to generate any thoughts. Fortunately, my teammates were patient and guided me through each step of the process. Gradually, I became adept at handling the code and successfully completed the task, for which I felt immensely grateful. This project made me realize the importance coding in the aviation industry like path planning, which is the field I aspire to work in. As a result, it has strengthened my determination to learn coding in the future.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Xie TianZhuo's Reflection:** At the beginning, I was very stressful when I received the task, because I had had no such experience in typing code. Meanwhile, my computer got some technical issue that I couldn’t set the environment variables for Python. I tried several times but failed. VScode and ‘py -m pip’ helped me solve the problem.  with the help of ChatGPT, I made a successful attempt by sending the requirements to ChatGPT. ChatGPT provided an initial page of code with some mistakes, and I continued to type my instructions. Finally, the code became more and more completed and satisfied the requirements. From my point of view, ChatGPT played an very important role in the task-solving progress. I could not handle the whole task without the help of ChatGPT. From this task, I learn that I need to continue to learn more about Python.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**'s Reflection:**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**'s Reflection:**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

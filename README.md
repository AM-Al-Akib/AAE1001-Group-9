# AAE1001-Group-9
# Presentation Link
*youtube link here


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents </h2></summary>
    <li><a href="#About-The-Project">About The Project </a></li>
    <li><a href="#Project-Video">Project Video </a></li>
    <li><a href="#Task-1">Task 1 </a></li>
    <li><a href="#Task-2">Task 2 </a></li>
    <li><a href="#Task-3">Task 3 </a></li>
    <li><a href="#Task-A1">Task A1 </a></li>
    <li><a href="#Task-A2">Task A2 </a></li>
    <li><a href="#Task-A3">Task A3 </a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
# Task A1
### Goal
"1. To add one checkpoint for each cost intensive area(2 in total) 2. To reach all checkpoints before arriving at the destination."

### Background
The primary goal is to deliver essential supplies to two separate locations. These supplies could range from medical and food supplies to technical equipment or humanitarian aid. Precise planning is essential, involving precise calculations for fuel, timing, and the safest and most efficient routes to reach the drop-off points and return to base. The primary mission of the supply craft is the swift and efficient delivery of crucial supplies to two high-priority, cost-intensive areas. Central to this mission is the strategic route planning, which focuses on creating the most direct and practical path between these checkpoints. This optimized routing is key to minimizing travel time and fuel consumption, ensuring the prompt delivery of essential items like medical and food supplies, and technical or humanitarian aid.

### Methodology 
In the given scenario from Task 1, our objective is to refine an existing pathfinding algorithm to automatically incorporate two designated checkpoints within cost-intensive areas. Modify our pathfinding algorithm to include these checkpoints as required waypoints. Once the optimal route is calculated, it should be visualized on the graph. This typically involves plotting the route over a map or graph, with checkpoints and cost-intensive areas clearly marked.

### Coding section
![node.cost](https://cdn.discordapp.com/attachments/901650593637101600/1180256309937963170/Screenshot_2023-12-02_032347.png?ex=657cc258&is=656a4d58&hm=cc2ea909e64dd01faad2074e13848b21cdc2f650c5e333bc11a03f1f0f14a2d2&)
To ensure the A* search algorithm routes the aircraft through the required checkpoints, we modify the 'self.fc_' attribute to represent the x and y coordinates of the two designated checkpoints. By setting the 'node.cost' to zero for these checkpoints, the algorithm is compelled to prioritize these waypoints, effectively guiding the aircraft through these specific locations without adding additional cost to the pathfinding calculation. This strategic adjustment allows the algorithm to seamlessly integrate the required checkpoints into the optimal route.
![plot](https://cdn.discordapp.com/attachments/901650593637101600/1180256309669544148/Screenshot_2023-12-02_032418.png?ex=657cc258&is=656a4d58&hm=76deb31ab3644f67f6e21bdabb1ff073fc6cae677acc6b5b18512a821c78374c&)
At this stage, we will visualize the two checkpoints by marking them in green on the plot.

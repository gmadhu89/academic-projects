This network visualization identifies similarity between board games from a simplified available dataset (calculated based on categories and game mechanics). The goal of this was to experiment the force-directed visual styling of this data using D3.js.  

Force-directed layouts use simulations of physical forces to arrange the elemnts(nodes in this case) on the screen. This is implemented using d3.forcesmimulation() module.  

Input file: board_games.csv  
Code: graph.html  

Execution Steps(to run in local):    
1) Copy the lib/ folder to your local.
2) Setup a local [http.server](https://ryanblunden.com/create-a-http-server-with-one-command-thanks-to-python-29fcfdcd240e)
3) Open graph.html after initiating http server to view the visualization.


![Snapshot of Visualization](https://github.com/gmadhu89/academic-projects/blob/main/force-directed-graph-visualization-d3/force-graph.JPG?raw=true "Snapshot of Visualization")

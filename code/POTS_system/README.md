## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model

The following figure shows the class diagram of the POTS model. 
At the beginning, some plants are created using `CreatePlants` function and then added to a `container` object. `Container` is setup with `gardenmixsoil`. The amount of water available for the whole system as rain, is defined at the beginning. This resource is not generated and will deplite over time.
When the simulation starts to run, at each 100<sup>th</sup> tick, some water will be added to the container as an effect of rain. Therefore, the available water in the sytem as rain is decreased at this tick.
The vegitables grow at each tick of the simulation by consuming the water and nutrient reserves of the container. If the plant does not get to have enough water or nutrients, the plant will die.

Weirdly the `Grow` function sets the amount of `sun` received to 0 at the grow function, therefore, the growth stops after the 1st tick. Moreover, the simulation does not check whether the plants are dead or alive before running the grow function.

### Class Diagram of POTS System
![POTS system](../../images/POTS%20System%20Class%20Diagram.png)

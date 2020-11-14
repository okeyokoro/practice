# Prompt

Imagine a robotic Bloom cafe in which coffees are prepared by a series of machines behind a
wall of cubbies. The machines (or stations) are organized into different station groups:
- Espresso machines,
- swirl and pour stations (milk and foam),
- sweetener stations,
- lidding stations, 
- and mechanical cubbies.

A fully-customized drink must pass from:
- an espresso machine to
- a swirl & pour station to
- a sweetener station to
- a lidding station and finally,
- to a cubby.

One issue that may arise is that a particular station may not be running
(for maintenance, cleaning, etc) and thus cannot accept a cup. Your task
is to find the shortest viable route from a given espresso station to a given cubby.

## Details

- Station positions are represented in a 3D graph.
  - You will need to calculate the distance between each station to determine your shortest route.
- Each station group may have more than one station.
  - For example, a swirl and pour group may contain 5 swirl and pour stations.
- Station-groups do not have to have the same amount of stations.
  - This should be clear from your input.
- The cup must hit every station-group.
- The cup will hit a station group only once.
- The cup will hit only one station per station-group.
- A station can pass a drink only to a station in the subsequent group.
  - ie, espresso stations pass only to swirl and pour stations
- A station can pass a cup to any of the stations at a subsequent group.
- Your input will be represented as a string (details below).

- Test your code by passing various espresso stations and cubbies to your shortestRoute().
- Test your code by altering your out-of-order stations.
- You don’t have to test/worry about the case in which all stations within a
 station-group are out-of-order.

## Input

- A multiline string that represents the machines and the cubbies.
- Each station group is demarcated by a new line.
  - The group order is as follows:
    - Expresso stations
    - Swirl & Pour stations
    - Sweetener stations
    - Lidding stations
    - Cubbies
- Each station within a group is demarcated by a semicolon.
- A station contains 4 bits of data in a "tuple":
  - (is running (1/0), x coordinate, y coordinate, z coordinate)

### kotlin

```
const val INPUT = """(1,-5,7,0);(1,-3,12,4);(1,0,8,2);(1,4,4,10)
(1,-9,2,3);(1,-4,0,0);(1,-1,1,2)
(1,-3,-5,5);(1,-1,-3,7);(0,4,-4,12);(1,8,-2,4);(1,10,-1, 3)
(1,-6,-7,2);(1,-1,-8,1);(1,3,-12,5);(1,9,-8,7)
(1,-5,-15,1);(1,-6,-16,8);(1,4,-15,1);(1,5,-17,2);(1,6,-15,9);(1,8,-15,7)"""
```

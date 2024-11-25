/* 
we need for loop
when runner complete 2 miles >> start at value 2
loop should stop give candy at 6 mile >> var i has to be equal to or grater then 6 
when the mile count reach to 6 
incrementing by to 2 
mileCount
 */

// Creating the function called runnerGetsCandy 
function runnerGetsCandy() {
    for (var mile = 2; mile <= 6; mile += 2) 
        console.log(`Ran" ${mile}  Miles here is your Candy`);
    
}
runnerGetsCandy();
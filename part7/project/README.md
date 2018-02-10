## Summary
This data visualization provides a graphical summary of which time of day/month of the year were the best to minimize flight delays. I've used [data](http://stat-computing.org/dataexpo/2009/) available for commercial flights within the USA, for years 1998, 2003 and 2008.
When a user chooses a year, the months with the highest and lowest median delay values are shown to guide visualization. After that, is it possible to highlight the months lines to compare delays with each other.

## Design
Initially, I've planned to show delays per time of day and weekdays, with lines corresponding to weekdays. However, this visualization does not made clear which season of the year or month could influence delays, so I've change the data shown in lines to be the months.

When all the lines were plotted, they  all were interlaced in a mess which could not allow readers distinguish its values. So, I've decided to reduce its opacity, and even change its color to gray, to only be highlighted when the mouse hover them. To ease this task, I've improved the line thick to contrast it over the other lines, with a small transition to look good. Also, I've added a text to instruct readers to hover the mouse over the lines.

Instead of using a fixed legend, binded to line colors, which could reduce graph area above the lines, I've decided to show the months names in the right side, at the lines ends. They are highlighted together with the lines hovered, making clear to which month they correspond.

To clarify which months are worst or best, in terms of median delays, I added a small animation, with tool tips over the highlighted months lines, with the median values for each of them.

Instead of using a fixed axis, showing delays values for the three years available, the scale is changed based on the year, allowing lines be more distributed over the graph height.


## Feedback

For the firsts sketches, I've received the following feedback of reader perception, some
of them have influenced design decisions listed above:
* It would be nice if it was possible to see information based on the season of year or month, to view influence of holidays, for example.
* It was difficult to distinguish relevant information when all month lines were plotted at the same time, overlaying each other, even using a different color palette.
* The fixed legend of the twelve months is ugly and space consuming.
* It was not clear that the reader needs to hover the mouse to highlight the lines.

After some improvements, that resulted in the final visualization, I've received these opinions:
* It is clearer that after midnight and before 06:00 is the best time for departures. In contrast, departures around 18:00 and 19:00 should be avoided. However, it is not clear what is the cause. There are more flights at night in comparison to the dawn?
* Values for the last time (23:00) on x axis could match those of the first time (0:00). It seems that exists something wrong with so disparate values, in some cases.
* It would be nice if the weather conditions were more clear, not only based on month/season.  It is clear that December is the worst month on 2003 and 2008, but it is not clear if was because of snowing or more people traveling on holidays.
* It would be nice if I've explored source or destination cities in the US.
* There are more delays than anticipations (negative delays over the y axis).
* It would be nice if the reader could see which flight companies have less delays, which could help which one to choose for next flights!

## Resources
1. https://stackoverflow.com/questions/23558701/d3-js-line-chart-with-time-on-both-axis
2. http://bl.ocks.org/d3noob/d8be922a10cb0b148cd5
3. https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep
4. https://amber.rbind.io/blog/2017/05/02/d3nest/
5. https://leanpub.com/d3-t-and-t-v4/read#leanpub-auto-get-tipping
6. http://bl.ocks.org/Matthew-Weber/5645518

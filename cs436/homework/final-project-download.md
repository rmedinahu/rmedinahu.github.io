---
layout: course_page
title: Final Project Data w/Instructions
permalink: /436/fp-data/
parent_course: 436
---


### The following code contains instructions on how to read/download external data into javascript. Please see the comments below on the specifics. 

> You will not have to modify your code very much but understand that the part of your code that processes the DATA array needs to be placed in the ```done``` function as noted below.

> If you get this to work then great. Submit before deadline. If not, then the final exam period (Dec. 6 3-5:50pm) should be sufficient for you complete this final project.

{% highlight javascript %}
<script type="text/javascript">
  $(document).ready(function() {
    
    /*
      Initialize up your isotope grid first. Yours may look a little different.
      Just make sure its the first block excecuted.
    */

    var $grid = $('#list').isotope({
      itemSelector: '.item',
      layoutMode: 'fitRows',
      getSortData: {
        date: '[data-date]', 
      }         
    }); 

    /* 
      All of your handy work with filter and sort button handlers etc., are here... 
    */


    /*  
      GET THE DATA:

      ADD the following code to the bottom of your script.
      
      EXPLANATION: The code below downloads the DATA array needed by your prototype. Because we
        don't know exactly WHEN the data will finish downloading we setup an EVENT handler to
        execute when the file is completely downloaded. This event handler is called "done". 
        You will want to place your DATA array processing code in the "done" function block.
        You can see my sample below.

      NOTE 1: The variable that the data is read into is named DATA. If your variable
        name for the sample data is different, you can adjust it accordingly below.

      NOTE 2: The code below needs to contain your code for processing the DATA array. 
        I am demonstrating one approach below. Most of you probably have that as well 
        other preprocessing on the DATA array. Please include that code in the "done" 
        function block (also noted in the explanation).

      NOTE 3: After data processing is complete make sure to "inform" the isotope library to add the
        items to its cache. See the last statement in the code below.

    */

    var url = "https://dl.dropboxusercontent.com/u/24668172/data-short-600.json";
    $.getJSON(url)
      .done(function(DATA) {  // This function is called when the DATA has completely downloaded.
        
        // create an array to hold our processed data items.
        var $items = [];  

        // loop through the DATA row, each time creating a div element and configuring as indicated.
        for (var i = 0; i < DATA.length; i++) {   
          var $itemrow = $("<div></div>")
            .addClass("col-md-12 item " + DATA[i][0] + " " + DATA[i][1] + " " + DATA[i][2])
            .attr("data-date", DATA[i][1])
            .html(DATA[i][0] + " " + DATA[i][1] + " " + DATA[i][2]);

          // add each configured div to the item array 
          $items.push($itemrow[0]); 
        }

      // after all processing is complete, update isotope with our item array.
      $grid.isotope().append( $items ).isotope( 'appended', $items);
    });

  });
</script>


{% endhighlight %}
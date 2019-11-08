  var barData = {
   labels : [{% for item in labels %}
      "{{item}}",
     {% endfor %}],
  datasets : [
     {
           fillColor: "rgba(151,187,205,0.2)",
           strokeColor: "rgba(151,187,205,1)",
           pointColor: "rgba(151,187,205,1)",
           data : [{% for item in values %}
            {{item}},
            {% endfor %}]
     } ]
  }
  
  var mychart = document.getElementById("chart").getContext("2d");
  steps = 10
  max = 100
  
  new Chart(mychart).Bar(barData, {
       scaleOverride: true,
       scaleSteps: steps,
       scaleStepWidth: Math.ceil(max / steps),
       scaleStartValue: 0,
       scaleShowVerticalLines: true,
       scaleShowGridLines : true,
       barShowStroke : true,
       scaleShowLabels: true
  });

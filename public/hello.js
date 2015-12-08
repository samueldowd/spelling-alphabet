$(document).ready(function() {
    // $.post( "https://daf4646lf2.execute-api.us-west-2.amazonaws.com/stage", {"test"}, alert("success"));

    $("#inputWord").on( "submit", function(e){ 
        e.preventDefault();
        var input = $(".radioInput").val();
        // var input_upper = input.toUpperCase();
        var params = '"'+ input + '"';

        console.log("input is " + params);
        // if ($.isPlainObject(params) == true) {
        // 	console.log("is a plainObject")
        // } else {
        // 	console.log("is not a plainObject")
        // };
        // alert(params);
         $.ajax({ 
         	 processData: false,
             type: "POST",
             // headers: {"Access-Control-Allow-Origin": "*"},
             dataType: "json",
             contentType: "plain/text",
             url: "https://daf4646lf2.execute-api.us-west-2.amazonaws.com/stage/",
             data: params,
             success: function(data){ 
             	$('#response p').remove();
             	var dataset = $.parseJSON(data);     
             	console.log("the body of the response is: ")
                console.log(dataset);
             	var i = 0
             	for(var i in dataset) { 
             		// console.log("the value of i is: " + i);
				    $( "#response" ).append("<p class='lineitem'><span class='letter text-uppercase'><strong>" + dataset[i][0] + "</strong></span> as in <span class='word'><strong>" + dataset[i][1] + "</strong><span></p>");
				};
             }
         });
    });
});
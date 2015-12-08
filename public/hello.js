$(document).ready(function() {
    // $.post( "https://daf4646lf2.execute-api.us-west-2.amazonaws.com/stage", {"test"}, alert("success"));

    $('#ajax').click(function(){ 
        
        var input = $("input").val();
        var input_upper = input.toUpperCase();
        var params = '"'+ input_upper + '"';

        // console.log(params)
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
             	console.log(dataset[1][1]);
             	console.log(dataset[-1]);
             	var i = 0
             	for(var i in dataset) { 
             		console.log("the value of i is: " + i)
				    $( "#response" ).append("<p><strong>" + dataset[i][0] + "</strong> as in <strong>" + dataset[i][1] + "</strong></p>");
				};
             }
         });
    });
});
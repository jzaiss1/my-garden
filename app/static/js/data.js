$(document).ready(function(){
    var template = $("#template").html();
    Mustache.parse(template);

    var rendered = Mustache.render(template, {
        preview: [
            {
                title: "One-of-a-Kind Coffee Table",
                abstract: "An industrial pulley and boat propellers may seem like an odd combination, but we have just the thing in mind... "
            },
            {
                title: "Overlooked Pieces",
                abstract: "Take an old wooden picture frame and a worn-out medicine cabinet to create something totally unique... "            
            },
            {
                title: "Crusty Cabinet",
                abstract: "Take an old worn-out yellow cabinet with potential despite the flaky paint job and worn wood and turn it into a shabby chic upgrade... "            
            },
            {
                title: "Wooden Wall Rack",
                abstract: "An old wooden wall hanging rack doesn't seem very exciting... until... "            
            }
        ]
    })
    $("#previewList").html(rendered);
});
var handleHeaderClick = function(e, column){
    $("#question-table").tabulator("setPage", 1); // show page 5
}

$(document).ready(function() {
    $("#question-table").tabulator({
        height: 600,
        width: "100%",
        responsiveLayout: "collapse",
        layout:"fitColumns", //fit columns to width of table (optional)
        columns:[
            {title:"Question", field:"question", headerClick:handleHeaderClick},
            {title:"Answer", field:"answer", align:"left", headerClick:handleHeaderClick}
        ],
        pagination: "remote",
        ajaxURL: "/rest/question",
        paginationSize: 20,
    });
});


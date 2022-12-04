$(document).ready(function(){
    $(".product-group-btn").click(function(){
        let list = $(this).next()
        if (list.hasClass("closed")) {
            $.ajax({
                url: '',
                type: 'get',
                data: {
                    product_group: $(this).attr("id")
                },
                success: function(response){
                    let categories = response.categories_to_return
                    $.each(categories,function(key, value){ 
                        $(list).append('<li><a class="dropdown-item category" href="#">' + value + '</a></li>');
                    });
                }
            });
            list.removeClass("closed")
        };    
    });

    $(".design-group-btn").click(function(){
        let list = $(this).next()
        if (list.hasClass("closed")) {
            $.ajax({
                url: '',
                type: 'get',
                data: {
                    design_group: $(this).attr("id")
                },
                success: function(response){
                    let designs = response.designs_to_return
                    $.each(designs,function(key, value){ 
                        $(list).append('<li><a class="dropdown-item category" href="#">' + value + '</a></li>');
                    });
                }
            });
            list.removeClass("closed")
        };    
    });


    let designGroupBtn = $(".design-btn-group").slice(1,4);
    designGroupBtn.removeClass("d-none");
    designGroupBtn.addClass("visible");

    $(".fa-chevrons-left").click(function(){
        let firstActive = $(".design-btn-group-wrapper").find(".visible:first");
        firstActive.addClass("foundFirst");

        let lastItemNext = $(".foundLast").next();
        if (lastItemNext.hasClass("fa-chevrons-right")) {
            $(".fa-chevrons-right").removeClass("d-none");
        }
        
        firstActive.prev(".design-btn-group").removeClass("d-none");
        firstActive.prev(".design-btn-group").addClass("visible");
        $(".foundFirst").removeClass("foundFirst");
        firstActive.prev(".design-btn-group").addClass("foundFirst");

        let firstItemPrev = $(".foundFirst").prev();
        if (firstItemPrev.hasClass("fa-chevrons-left")) {
            $(".fa-chevrons-left").addClass("d-none");
        }
        
        let lastActive = $(".design-btn-group-wrapper").find(".visible:last");
        lastActive.addClass("foundLast")
        lastActive.removeClass("visible");
        lastActive.addClass("d-none");
        lastActive.removeClass("foundLast");
        lastActive.prev(".design-btn-group").addClass("foundLast");

    });
    $(".fa-chevrons-right").click(function(){
        let firstActive = $(".design-btn-group-wrapper").find(".visible:first");
        firstActive.addClass("foundFirst");
        let firstItemPrev = $(".foundFirst").prev();
        if (firstItemPrev.hasClass("fa-chevrons-left")) {
            $(".fa-chevrons-left").removeClass("d-none");
        }
        firstActive.removeClass("visible");
        firstActive.addClass("d-none");
        firstActive.removeClass("foundFirst");
        firstActive.next(".design-btn-group").addClass("foundFirst");

        let lastActive = $(".design-btn-group-wrapper").find(".visible:last");
        lastActive.addClass("foundLast")
        lastActive.next(".design-btn-group").removeClass("d-none");
        lastActive.next(".design-btn-group").addClass("visible");
        lastActive.removeClass("foundLast");
        lastActive.next(".design-btn-group").addClass("foundLast");
        let lastItemNext = $(".foundLast").next();
        if (lastItemNext.hasClass("fa-chevrons-right")) {
            $(".fa-chevrons-right").addClass("d-none");
        }
   });

});
$(function(){
    $(".next_img_btn").click(function(){
        var $active_img = $(".active");
        var $next_img = $active_img.next();
        if ($next_img.is("li")){
            $active_img.removeClass("active").addClass("hide");
            $next_img.removeClass("hide").addClass("active");
        }
    });
    $(".prev_img_btn").click(function(){
        var $active_img = $(".active");
        var $next_img = $active_img.prev();
        if ($next_img.is("li")){
            $active_img.removeClass("active").addClass("hide");
            $next_img.removeClass("hide").addClass("active");
        }
    });
});
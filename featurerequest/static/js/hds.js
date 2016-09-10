$('#navigation.nav-pills li a').click(function() {
    var route = $(this).attr('href');
    $("#navigation.nav-pills li.active").removeClass("active");
    $(this).addClass("active"); 
});

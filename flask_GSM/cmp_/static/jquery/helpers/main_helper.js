jQuery.fn.isMobile = function() {
    var ua = navigator.userAgent;
    var isValid = false;
    var checker = {
        iphone: ua.match(/(iPhone|iPod|iPad)/),
        blackberry: ua.match(/BlackBerry/),
        android: ua.match(/Android/)
    };
    if (checker.android) {
        isValid = true;
    } else if (checker.iphone) {
        isValid = true;
    } else if (checker.blackberry) {
        isValid = true;
    }

    return isValid;
};
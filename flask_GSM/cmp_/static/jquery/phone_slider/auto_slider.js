$(document).ready(function() {
    var animateDelay = 300;

    function slide_left() {

    }

    function slide_right() {

    }

    $('.corousel-container .slider-arrow .previous').click(function(e) {
        let $parent = $(e.currentTarget).parent();
        let $row;
        let sibling_width;
        let current_scroll;
        if ($parent.length > 0) {
            $row = $($parent[0]).parent('.row');
            let $sibling = $($parent[0]).siblings('.block-content');
            sibling_width = $sibling.length > 0 ? $($sibling[0]).outerWidth(true) : 50;
            $parent.siblings('.slider-arrow').show();
        }
        current_scroll = $row.scrollLeft();
        if (current_scroll - sibling_width <= 0) {
            $row.animate({ scrollLeft: 0 }, animateDelay, 'swing');
        } else {
            $row.animate({ scrollLeft: current_scroll - sibling_width }, animateDelay, 'swing');
        }
    });

    $('.corousel-container .slider-arrow .next').click(function(e) {
        let $parent = $(e.currentTarget).parent();
        let $row;
        let sibling_width;
        let current_scroll;
        let scroll_width;
        if ($parent.length > 0) {
            $row = $($parent[0]).parent('.row');
            let $sibling = $($parent[0]).siblings('.block-content');
            sibling_width = $sibling.length > 0 ? $($sibling[0]).outerWidth(true) : 50;
            $parent.siblings('.slider-arrow').show();
        }
        current_scroll = $row.scrollLeft();
        scroll_width = $row.length > 0 ? $row[0].scrollWidth - $row[0].clientWidth : 0;
        if (current_scroll + sibling_width <= scroll_width) {
            $row.animate({ scrollLeft: current_scroll + sibling_width }, animateDelay, 'swing');
        } else {
            $row.animate({ scrollLeft: scroll_width }, animateDelay, 'swing');
        }
    });
});
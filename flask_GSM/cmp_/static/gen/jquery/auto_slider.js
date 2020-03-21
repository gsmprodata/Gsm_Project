$(document).ready(function() {
    var animateDelay = 300;
    var autoScrollTimer = 1500;
    var isSliderPaused = false;
    var processorBrandUrl = $('#hdnInpFilterUrls').data('processorBrandsUrl')

    function populateProcessorBrandDropDown() {
        $.ajax({
            type: "GET",
            url: processorBrandUrl,
            // dataType:"json",
            success: function(data) {
                let options = '<option>Select</option>';
                $.each(data, function(key, item) {
                    options += `<option value="${item.id}">${item.name}</option>`;
                });
                $('#ddlProcessorBrand').html(options);
            },
            error: function(data) {
                alert('error');
            }
        });
    }

    function slide_left() {
        let $parent = $('.corousel-container .slider-arrow .previous').parent()
        let $row;
        let auto_scroll_left;
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
            auto_scroll_left = false;
        } else {
            $row.animate({ scrollLeft: current_scroll - sibling_width }, animateDelay, 'swing');
            auto_scroll_left = true;
        }
        return auto_scroll_left;
    }

    function slide_right() {
        let $parent = $('.corousel-container .slider-arrow .next').parent()
        let $row;
        let sibling_width;
        let auto_scroll_right;
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
            auto_scroll_right = true;
        } else {
            $row.animate({ scrollLeft: scroll_width }, animateDelay, 'swing');
            auto_scroll_right = false;
        }
        return auto_scroll_right;
    }

    function autoScroll(auto_scroll_left, auto_scroll_right) {
        let scroll_right;
        let scroll_left;
        if (auto_scroll_right && !$().isMobile()) {
            if (isSliderPaused) {
                scroll_right = true;
            } else {
                scroll_right = slide_right();
            }
            setTimeout(function() {
                if (scroll_right) {
                    autoScroll(false, scroll_right)
                } else {
                    autoScroll(true, scroll_right)
                }

            }, autoScrollTimer);
            return true;
        }

        if (auto_scroll_left && !$().isMobile()) {
            if (isSliderPaused) {
                scroll_left = true;
            } else {
                scroll_left = slide_left();
            }
            setTimeout(function() {
                if (scroll_left) {
                    autoScroll(scroll_left, false)
                } else {
                    autoScroll(scroll_left, true)
                }
            }, autoScrollTimer);
            return true;
        }

    }

    setTimeout(function() {
        autoScroll(false, true);
    }, autoScrollTimer)

    $('.corousel-container .slider-arrow .previous').click(function(e) {
        slide_left();
    });

    $('.corousel-container .slider-arrow .next').click(function(e) {
        slide_right();
    });

    $('.corousel-container .row').on("mouseenter", function() {
        isSliderPaused = true;
    })
    $('.corousel-container .row').on("mouseleave", function() {
        isSliderPaused = false;
    })

    populateProcessorBrandDropDown();
});
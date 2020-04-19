from  cmp_ import app
from flask_assets import Environment, Bundle

assets = Environment(app)

main_js = Bundle('jquery/main.js', 'jquery/helpers/main_helper.js', 'jquery/jquery-ui-1.12.1.custom/jquery-ui.min.js', output='gen/jquery/main.js' )
assets.register('main_js', main_js)

filter_js = Bundle('', filters='jsmin',  output='gen/jquery/filter.js' )
assets.register('filter_js', filter_js)

filter_css = Bundle('', filters='cssmin',  output='gen/css/filter.css' )
assets.register('filter_css', filter_css)

autoslider_js = Bundle('jquery/phone_slider/auto_slider.js',  filters='jsmin', output='gen/jquery/auto_slider.js' )
assets.register('autoslider_js', autoslider_js)

main_css = Bundle('css/main.css', 'css/responsive-mobile.css', 'css/responsive-tablet.css', 'css/all.css', 'jquery/jquery-ui-1.12.1.custom/jquery-ui.min.css', filters='cssmin',  output='gen/css/main.css' )
assets.register('main_css', main_css)

phone_detail_js = Bundle('jquery/phone_detail/index.js', filters='jsmin',  output='gen/jquery/phone_details.js' )
assets.register('phone_detail_js', phone_detail_js)



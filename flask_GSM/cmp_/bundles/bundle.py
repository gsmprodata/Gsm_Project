from  cmp_ import app
from flask_assets import Environment, Bundle

assets = Environment(app)

main_js = Bundle('jquery/main.js', 'jquery/helpers/main_helper.js', filters='jsmin',  output='gen/jquery/main.js' )
assets.register('main_js', main_js)


main_css = Bundle('css/main.css', 'css/responsive-mobile.css', 'css/responsive-tablet.css', filters='cssmin',  output='gen/css/main.css' )
assets.register('main_css', main_css)

phone_detail_js = Bundle('jquery/phone_detail/index.js', filters='jsmin',  output='gen/jquery/phone_details.js' )
assets.register('phone_detail_js', phone_detail_js)



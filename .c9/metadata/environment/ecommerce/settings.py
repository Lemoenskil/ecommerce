{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":62,"position":62,"stack":[[{"start":{"row":43,"column":11},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":80},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":6},"action":"insert","lines":["''"],"id":81}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":[" "],"id":82}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"remove","lines":[" "],"id":83}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["c"],"id":84},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["h"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["e"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["c"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["k"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["o"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["u"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":[","],"id":85}],[{"start":{"row":13,"column":10},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":86},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["i"]},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["p"],"id":87},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["o"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["r"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":[" "],"id":88},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["d"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["j"]}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["-"],"id":89}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["-"],"id":90}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["_"],"id":91},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["d"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["a"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["a"],"id":92},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["b"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["a"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["s"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["_"],"id":93},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["u"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["r"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["k"]}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["k"],"id":94}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["l"],"id":95}],[{"start":{"row":81,"column":0},"end":{"row":89,"column":1},"action":"remove","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}"],"id":96},{"start":{"row":81,"column":0},"end":{"row":91,"column":78},"action":"insert","lines":["# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":65},"action":"remove","lines":["'c3)@(j1kaij1em2uibnsw!s7jqthhj^csl#&!k@(g7qyu&-+y@'"],"id":97},{"start":{"row":24,"column":13},"end":{"row":24,"column":41},"action":"insert","lines":["os.environ.get('SECRET_KEY')"]}],[{"start":{"row":14,"column":22},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":98}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":22},"action":"insert","lines":["import dj_database_url"],"id":99}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":22},"action":"remove","lines":["import dj_database_url"],"id":100}],[{"start":{"row":46,"column":15},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":101},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["`"]}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":[" "],"id":102}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"remove","lines":[" "],"id":103}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["S"],"id":104},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["t"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"remove","lines":["o"],"id":105},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"remove","lines":["t"]},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"remove","lines":["S"]}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["s"],"id":106},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["t"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["o"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["r"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["a"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["g"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["e"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["`"],"id":107}],[{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":[" "],"id":108}],[{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"remove","lines":[" "],"id":109},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"remove","lines":["`"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"remove","lines":["s"]}],[{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["s"],"id":110}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"remove","lines":["`"],"id":111}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["'"],"id":112}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["`"],"id":113}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"remove","lines":["`"],"id":114}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["'"],"id":115},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":[","]}],[{"start":{"row":131,"column":0},"end":{"row":143,"column":64},"action":"insert","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl': 'max-age=94608000'","}","","AWS_STORAGE_BUCKET_NAME = 'ecommerce'","AWS_S3_REGION_NAME = 'eu-west-1'","AWS_ACCESS_KEY_ID = os.environ.get(\"AWS_ACCESS_KEY_ID\")","AWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","","STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'"],"id":116}],[{"start":{"row":143,"column":64},"end":{"row":144,"column":0},"action":"insert","lines":["",""],"id":117}],[{"start":{"row":130,"column":60},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":118}],[{"start":{"row":137,"column":27},"end":{"row":137,"column":36},"action":"remove","lines":["ecommerce"],"id":119},{"start":{"row":137,"column":27},"end":{"row":137,"column":52},"action":"insert","lines":["code-institude-e-commerce"]}],[{"start":{"row":138,"column":30},"end":{"row":138,"column":31},"action":"remove","lines":["1"],"id":120},{"start":{"row":138,"column":29},"end":{"row":138,"column":30},"action":"remove","lines":["-"]},{"start":{"row":138,"column":28},"end":{"row":138,"column":29},"action":"remove","lines":["t"]},{"start":{"row":138,"column":27},"end":{"row":138,"column":28},"action":"remove","lines":["s"]},{"start":{"row":138,"column":26},"end":{"row":138,"column":27},"action":"remove","lines":["e"]},{"start":{"row":138,"column":25},"end":{"row":138,"column":26},"action":"remove","lines":["w"]},{"start":{"row":138,"column":24},"end":{"row":138,"column":25},"action":"remove","lines":["-"]},{"start":{"row":138,"column":23},"end":{"row":138,"column":24},"action":"remove","lines":["u"]},{"start":{"row":138,"column":22},"end":{"row":138,"column":23},"action":"remove","lines":["e"]}],[{"start":{"row":138,"column":22},"end":{"row":138,"column":49},"action":"insert","lines":["EU (Frankfurt) eu-central-1"],"id":121}],[{"start":{"row":138,"column":36},"end":{"row":138,"column":37},"action":"remove","lines":[" "],"id":122},{"start":{"row":138,"column":35},"end":{"row":138,"column":36},"action":"remove","lines":[")"]},{"start":{"row":138,"column":34},"end":{"row":138,"column":35},"action":"remove","lines":["t"]},{"start":{"row":138,"column":33},"end":{"row":138,"column":34},"action":"remove","lines":["r"]},{"start":{"row":138,"column":32},"end":{"row":138,"column":33},"action":"remove","lines":["u"]},{"start":{"row":138,"column":31},"end":{"row":138,"column":32},"action":"remove","lines":["f"]},{"start":{"row":138,"column":30},"end":{"row":138,"column":31},"action":"remove","lines":["k"]},{"start":{"row":138,"column":29},"end":{"row":138,"column":30},"action":"remove","lines":["n"]},{"start":{"row":138,"column":28},"end":{"row":138,"column":29},"action":"remove","lines":["a"]},{"start":{"row":138,"column":27},"end":{"row":138,"column":28},"action":"remove","lines":["r"]}],[{"start":{"row":138,"column":26},"end":{"row":138,"column":27},"action":"remove","lines":["F"],"id":123},{"start":{"row":138,"column":25},"end":{"row":138,"column":26},"action":"remove","lines":["("]},{"start":{"row":138,"column":24},"end":{"row":138,"column":25},"action":"remove","lines":[" "]},{"start":{"row":138,"column":23},"end":{"row":138,"column":24},"action":"remove","lines":["U"]},{"start":{"row":138,"column":22},"end":{"row":138,"column":23},"action":"remove","lines":["E"]}],[{"start":{"row":144,"column":0},"end":{"row":144,"column":64},"action":"remove","lines":["STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'"],"id":124},{"start":{"row":144,"column":0},"end":{"row":145,"column":53},"action":"insert","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'"]}],[{"start":{"row":158,"column":21},"end":{"row":159,"column":0},"action":"insert","lines":["",""],"id":126},{"start":{"row":159,"column":0},"end":{"row":160,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":160,"column":0},"end":{"row":161,"column":53},"action":"insert","lines":["MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":127}],[{"start":{"row":157,"column":0},"end":{"row":161,"column":53},"action":"remove","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'","","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":129},{"start":{"row":157,"column":0},"end":{"row":161,"column":74},"action":"insert","lines":["MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"]}],[{"start":{"row":86,"column":0},"end":{"row":93,"column":78},"action":"remove","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":130},{"start":{"row":86,"column":0},"end":{"row":96,"column":0},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":10},"action":"remove","lines":["import env"],"id":131}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":132}],[{"start":{"row":29,"column":89},"end":{"row":29,"column":90},"action":"insert","lines":[","],"id":133}],[{"start":{"row":29,"column":90},"end":{"row":29,"column":92},"action":"insert","lines":["\"\""],"id":134}],[{"start":{"row":29,"column":90},"end":{"row":29,"column":92},"action":"remove","lines":["\"\""],"id":135}],[{"start":{"row":29,"column":90},"end":{"row":29,"column":92},"action":"insert","lines":["''"],"id":136}],[{"start":{"row":29,"column":91},"end":{"row":29,"column":135},"action":"insert","lines":["ecommerce-yvette-exercise-test.herokuapp.com"],"id":137}],[{"start":{"row":13,"column":22},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":138},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["f"]},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["r"]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["o"]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":[" "],"id":139},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["n"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["v"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":[" "],"id":140},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["m"],"id":141}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["i"],"id":142},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["m"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["p"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["o"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["r"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":[" "],"id":143},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["*"]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["from env import *",""],"id":144},{"start":{"row":14,"column":0},"end":{"row":15,"column":11},"action":"insert","lines":["if os.path.exists('env.py'):","\timport env"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":11},"end":{"row":15,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590997572526,"hash":"fadfdd11be23dd98a68743f8ad266b8d4bb24fa3"}
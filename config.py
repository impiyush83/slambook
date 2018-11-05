import os

if os.environ.get("SLAMBOOK_ENV") == 'dev':
    db_url = 'postgresql://slambook:slambook@localhost:9011/slambook_dev'
else:
    db_url = 'postgresql://slambook:slambook@localhost:9011/slambook_test'

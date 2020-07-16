#!/usr/bin/python3

import subprocess
import shlex
import shutil
import json

index='''
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="fluid_style.css">
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato%3A300%2C300italic%2C400%2C400italic%2C700%2C700italic&display=swap">
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-W8TXVP5YQW"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-W8TXVP5YQW'); </script>
<!-- update the version number as needed -->
<script defer src="/__/firebase/7.9.3/firebase-app.js"></script>
<!-- include only the Firebase features as you need -->
<script defer src="/__/firebase/7.9.3/firebase-auth.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-database.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-messaging.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-storage.js"></script>
<!-- initialize the SDK after all desired features are loaded -->
<script defer src="/__/firebase/init.js"></script>
</head>
<body>

	<div class="fluid_sidebar">
		<h1><a href="https://www.fluidnumerics.com">Fluid Numerics</a></h1>
	</div>

	<div class="fluid_header">
		<h1>Fluid Slurm-GCP Codelabs</h1>
	</div>

	<div class="fluid_body">

	    <h2><a href="https://www.fluidnumerics.com">Head back to Fluid Numerics</a></h2>

        </div>

        <div class="fluid_footer">
            <h2>Let us know if we can do anything to improve these codelabs!</h2>
            <h3><a href="https://forms.gle/q5HaN43HyVXLSLmM9">Submit your feedback here</a></h3>
        </div>
</body>
</html>
'''

firebase_txt='''
<!-- update the version number as needed -->
<script defer src="/__/firebase/7.9.3/firebase-app.js"></script>
<!-- include only the Firebase features as you need -->
<script defer src="/__/firebase/7.9.3/firebase-auth.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-database.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-messaging.js"></script>
<script defer src="/__/firebase/7.9.3/firebase-storage.js"></script>
<!-- initialize the SDK after all desired features are loaded -->
<script defer src="/__/firebase/init.js"></script>
'''

def inject_firebase(subdirectory):

    filepath = subdirectory+'/index.html'
    cl_index = []
    with open(filepath) as fp:
        line = fp.readline()
        cl_index.append(line)
        cnt = 1
        while line:
            line = fp.readline()
            cl_index.append(line)
            if '</style>' in line:
                cl_index.append(firebase_txt)
            cnt += 1

    f=open(filepath,'w')
    f.write('\n'.join(cl_index))
    f.close()
    
#END inject_firebase

def update_codelabs():

    with open('./docs.json') as f:
        config = json.load(f)

    # Update tutorials
    for tutorial in config['docs']:
        print('Updating {}'.format(tutorial['title']))
        subprocess.check_call(shlex.split('mkdir -p public/{}'.format(tutorial['subdirectory'])))
        subprocess.check_call(shlex.split('./tools/claat/claat-linux-amd64 export {}'.format(tutorial['gdoc_id'])))
        subprocess.check_call(shlex.split('rm -rf public/{}'.format(tutorial['subdirectory'])))
        shutil.copytree('URL/', 'public/{}'.format(tutorial['subdirectory']))
        inject_firebase('public/{}'.format(tutorial['subdirectory']))
        subprocess.check_call(shlex.split('rm -rf URL/'.format(tutorial['subdirectory'])))

#END update_codelabs

def main():

    update_codelabs()


#END main

if __name__ == '__main__':
    main()


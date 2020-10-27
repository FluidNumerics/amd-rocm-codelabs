# AMD ROCm Codelabs 
This repository contains the static pages for the [AMD-ROCm Codelabs](https://fluid-amd-codelabs.web.app/) in addition to tools to quickly generate codelabs from Google Docs.


## How to contribute

### [Join the AMD ROCm Codelab Developer Team](https://docs.google.com/forms/d/e/1FAIpQLSeIDbLse_tSHJFPb7Fo4M0pPJgoUHRTFnU4o-CNzEPTp_ohbw/viewform?usp=sf_link)
If you'd like to become a codelab developer/contributor, [sign up to join the AMD ROCm Codelab Developer team](https://docs.google.com/forms/d/e/1FAIpQLSeIDbLse_tSHJFPb7Fo4M0pPJgoUHRTFnU4o-CNzEPTp_ohbw/viewform?usp=sf_link).

### Provide Feedback
If you have questions, comments, or suggestions you can help inspire conversation and improve these codelabs by opening issues on this repository's issue tracker.

### Current Codelabs - Google Docs
* [Building a basic GPU accelerated application with HIP in C/C++](https://docs.google.com/document/d/1GYt1m-GJx1M9VFVIeOT90XbXKACoUhT1wu94jGc_9NY)
* [Building a basic GPU accelerated application with OpenMP in C/C++](https://docs.google.com/document/d/15W_7Z1BMyMXmqjXYZ2flVmm1evvTA4fEzkihFBZ3jEc)


### Generate Codelabs
Codelabs are written in Google Docs following the [Codelabs formatting guidelines](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md). Once codelabs are written, the Google Docs can be converted to html using the claat command-line tool. A binary for claat for Linux x86 platforms is provided in this repository under [tools/claat/](tools/claat/).

To generate the codelab documentation, simply run
```
python3 gen_docs.py
```
This will create/update the html codelabs underneath the `public/` subdirectory.
Note that you must have a Gmail, GSuite, or Cloud Identity account with Viewer access to the Google Docs listed in [`docs.json`](./docs.json).



# AMD ROCm Codelabs 

This repository contains Codelab demos, [accompanying example source code](./code/), and tools for generating the Codelabs from Google Docs [(claat)](https://github.com/googlecodelabs/tools).


## Help Improve These Codelabs
If you have questions, comments, or suggestions you can help inspire conversation and improve these codelabs by opening issues on this repository's issue tracker.

## Contributing Codelabs

### Current Codelabs - Google Docs
All of our codelabs are drafted in Google Docs and then processed with [claat](./tools/claat) to generate the html files for the codelabs. The Google Docs for our current codelabs can be found using the links below

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


### How to contribute
If you'd like to contribute a codelab, reach out to support@fluidnumerics.com for view access to Google Docs for existing codelabs in this repository.

1. Clone this repository and create a new branch off of master.
2. Create a Codelab in Google Docs following the [Codelabs formatting guidelines](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md).
3. Add a doc block to [`docs.json`](./docs.json) that details the required metadata.
4. Run `python3 gen_docs.py`
5. `git add docs.json public/ && git commit && git push -u origin BRANCH-NAME`
6. Open a pull request to master

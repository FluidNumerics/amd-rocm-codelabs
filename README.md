# AMD Codelabs 

This repository contains Codelab demos, accompanying example source code, and tools for generating the Codelabs from Google Docs [(claat)](https://github.com/googlecodelabs/tools).


## Generate Codelabs
Codelabs are written in Google Docs following the [Codelabs formatting guidelines](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md). Once codelabs are written, the Google Docs can be converted to html using the claat command-line tool. A binary for claat for Linux x86 platforms is provided in this repository under [tools/claat/](tools/claat/).

To generate the codelab documentation, simply run
```
python3 gen_docs.py
```
This will create/update the html codelabs underneath the `public/` subdirectory.
Note that you must have a Gmail, GSuite, or Cloud Identity account with Viewer access to the Google Docs listed in [`docs.json`](./docs.json).


## Contributing a Codelab
If you'd like to contribute a codelab, reach out to support@fluidnumerics.com for view access to Google Docs for existing codelabs in this repository. Then,
1. Clone this repository and create a new branch off of master.
2. Create a Codelab in Google Docs following the [Codelabs formatting guidelines](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md).
3. Add a doc block to [`docs.json`](./docs.json) that details the required metadata
4. Run `python3 gen_docs.py`
5. `git add docs.json public/ && git commit && git push -u origin BRANCH-NAME`
6. Open a pull request to master



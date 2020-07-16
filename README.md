# AMD Codelabs 

This repository contains Codelab demos, accompanying example source code, and tools for generating the Codelabs from Google Docs (claat).


## Generate Codelabs
Codelabs are written in Google Docs following the Codelabs formatting guidelines. Once codelabs are written, the Google Docs can be converted to html using the claat command-line tool. A binary for claat for Linux x86 platforms is provided in this repository under [tools/claat/](tools/claat/).

To generate the codelab documentation, simply run
```
./tools/claat/claat-linux-amd64 export GDOC-ID
```
where `GDOC-ID` is the Google Doc ID. Note that you must have a Gmail, GSuite, or Cloud Identity account with Viewer access to the Google Doc associated with `GDOC-ID`.

See `docs.json` for a listing of the Google Docs under version control in this repository.


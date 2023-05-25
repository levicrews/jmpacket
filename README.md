# jmpacket

*Disclaimer*: I compiled this repository in the spring after my job market season. It exists to help other UChicago econ PhDs prepare for the market. If you find a bug or think of an improvement, feel free to submit an issue, but please keep in mind that **I don't plan to actively maintain this repo**. That said, I'll do my best to review and merge pull requests if you're able to implement the change yourself.

---

A typical job market packet for the academic econ market consists of the following:

1. JMP
2. spiel
3. job talk
4. CV
5. website
6. cover letters
7. statements (research, teaching, DEIB)
8. other research outputs
9. application forms/profiles
10. letters of recommendation

**This repository provides code and templates to help you produce your spiel (#2), CV (#4), cover letters (#6), and statements (#7).** For JMP (#1) and job talk (#3) templates, see my [repository](https://github.com/levicrews/crews-latex) of LaTeX style files. For a website (#5) template, see my [fork](https://github.com/levicrews/academic-website) of the Hugo Academic template.

Here's an annotated file tree for this repository:

```
.
├── coverletters
│   ├── compile.py                                    * script to compile one customized cover letter for each job
│   ├── coverletter.tex
│   ├── jobs.csv                                      * list of jobs and their attributes to insert in cover letters
│   └── uchicagologo.png
├── cv
│   ├── <lastname>_cv.pdf
│   ├── <lastname>_cv.tex                             * a nicer CV
│   ├── <lastname>_cv-uchicagoformat.docx             * mandatory UChicago CV template
│   ├── <lastname>_cv-uchicagoformat.pdf
│   └── res.cls                                       * class for a nicer CV
├── jmIDs.tex                                         * LaTeX commands for your repeated ID elements (to be symlinked)
├── jmstatement.cls                                   * common class for your statements and spiel (to be symlinked)
├── panel.pdf                                         * slides with advice for the job market (UChicago, May 2023)
├── spiel                                             * interview spiel
│   ├── <lastname>_spiel.pdf
│   └── <lastname>_spiel.tex
├── statement_deib                                    * Diversity, Equity, Inclusion, & Belonging statement
│   ├── <lastname>_deib.pdf
│   └── <lastname>_deib.tex
│   └── notes_deib.org
├── statement_research                                * research statement
│   ├── <lastname>_research.pdf
│   └── <lastname>_research.tex
└── statement_teaching                                * teaching statement (experience + philosophy)
    ├── <lastname>_teach.pdf
    └── <lastname>_teach.tex
    └── notes_teach.org
```

## Getting started

1. **Clone this repository**. If you don't want to use Git, you can download the repository as a ZIP file.

2. **Install the dependencies**. Almost surely your machine already has LaTeX and Python installed. If not, install them. For Python, I recommend downloading [Anaconda](https://www.anaconda.com/). You can find the necessary LaTeX and Python packages in the preambles of the `.tex`/`.cls` files and `compile.py`, respectively.

3. **Symlink** (`ln -s`) the class `jmstatement.cls` and the command file `jmIDs.tex` into the relevant subdirectories:

   - `/spiel`
   - `/statement_deib`
   - `/statement_research`
   - `/statement_teaching`
   - only for `jmIDs.tex`:
     - `/cv`
     - `/coverletters`

4. **Fill in `jmIDs.tex` and customize `jmstatement.cls`**. Fill in the commands for your name, your fields, your one-sentence ID, and your three-sentence ID (refer to `panel.pdf` if you don't know what I'm talking about). Change the margins, link colors, or whatever else. *Note: Edit the files in the root directory*. Your changes will automatically propagate to the subdirectories through the symlinks.

## CV, spiel, and statements

- **Fill in your CV**. The UChicago placement committee will insist that you make a version using their `.docx` template so they can include it in the department's packet. I think it looks awful and I hate Microsoft Word. For your own applications and website, I recommend producing a nicer CV in LaTeX using the `res.cls` class.

- At this point, you can **write your spiel or any of your statements**, since none of them will be customized for individual job postings. The corresponding `.tex` files are peppered with comments to help you adapt my statements and spiel into your own. For the DEIB and teaching statements, I've included additional files of notes pulled from other sources.

## Cover letters

1. **Gather job postings**. At UChicago, you'll be given a Google Sheet that you and your committee (read: their assistants) will use to track your letters of recommendation for each job posting. The sheet will have spots to list the sector, institution, department, and job title for each posting. Most academic postings for the U.S. will be on the AEA's [JOE](https://www.aeaweb.org/joe/listings) or on [EJM](https://econjobmarket.org/), but you'll likely need to search more widely, too. Consider using Benjamin Vatter's [JobMarketTracker](https://github.com/benjaminvatterj/JobMarketTracker).

2. **Fill in `coverletters/jobs.csv`**. Open `jobs.csv` and explore the example entries. The CSV comes with nine columns (delimited by pipes `|`), each of which corresponds to a LaTeX command used in `coverletter.tex` or a variable in `compile.py`.

   | Variable       | Description                                                     |
   |----------------|-----------------------------------------------------------------|
   | `uploaded`     | Boolean indicating whether you've uploaded the application      |
   | `uniqueID`     | ID for the posting to name the PDF `coverletter_<uniqueID>.pdf` |
   | `salutation`   | How you want to address the recipient                           |
   | `jobtitle`     | "I am writing to apply for the position of `jobtitle` at ..."   |
   | `institution`  | "... the position of `jobtitle` at `institution`."              |
   | `fit`          | Brief, general statement why you're a good fit for the position |
   | `teaching`     | Select which description of your teaching to include (if any)   |
   | `customCLskip` | Size of vertical skip to ensure letter stays on one page        |
   | `fourthLOR`    | Name of fourth letter writer (some postings have max of three)  |
   | `desire`       | Specific reason you want that job (e.g., location constraints)  |

   Add entries by copying over postings from your Google Sheet and filling in the remaining columns. You can add any new LaTeX command to the program by adding a column to the jobs spreadsheet and then invoking the LaTeX command in the appropriate spot in `coverletter.tex`. Once you've uploaded a cover letter to the relevant application portal, mark the `uploaded` column as `True` to prevent the script from overwriting the PDF.

3. **Generate example letters by running `compile.py`**. You'll generate ~25 letters that I sent to various academic positions and public sector research jobs. I suggest you create and move them into a subdirectory called `/examples` to store them for easy reference later.

4. **Customize the `compile.py` script**. The script is pretty simple, but you may want to change the default filepaths, for instance. It may not be the most robust, either, so don't be surprised if you need to fix weird edge cases.

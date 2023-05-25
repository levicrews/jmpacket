# %% load packages
import pandas as pd
import os
import subprocess
import glob
# %% set LaTeX info
tex_filename = 'coverletter.tex'
filename, ext = os.path.splitext(tex_filename)
# %% read in jobs.csv
jobs     = pd.read_csv('jobs.csv', delimiter='|', keep_default_na=False)
jobstodo = jobs[jobs['uploaded']==False]
# %% compile coverletter for each job
for index, job in jobstodo.iterrows():

    uniqueID = job['uniqueID']

    # write custom commands to currentjob.tex (overwriting previous version)
    f = open("currentjob.tex", "w")
    f.write("\\newcommand{\\salutation}{%s}\n" % job['salutation'])
    f.write("\\newcommand{\\jobtitle}{%s}\n" % job['jobtitle'])
    f.write("\\newcommand{\\institution}{%s}\n" % job['institution'])
    f.write("\\newcommand{\\fit}{%s}\n" % job['fit'])
    f.write("\\newcommand{\\teaching}{%s}\n" % job['teaching'])
    f.write("\\newcommand{\\customCLskip}{%s}\n" % job['customCLskip'])
    f.write("\\newcommand{\\desire}{%s}" % job['desire'])
    f.close()

    # compile TeX file
    pdf_filestub = filename + '_' + uniqueID
    pdf_jobname  = '-jobname=' + pdf_filestub
    pdf_filename = pdf_filestub + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', pdf_jobname, tex_filename])

    # check if PDF is successfully generated
    if not os.path.exists(pdf_filename):
        raise RuntimeError('PDF output not found')

#%% delete any auxiliary files
types = ['*.aux', '*.bbl', '*.blg', '*.idx', '*.ind', '*.lof', '*.lot', '*.out',
         '*.toc', '*.acn', '*.acr', '*.alg', '*.glg', '*.glo', '*.gls', '*.fls',
         '*.log', '*.fdb_latexmk', '*.snm', '*.synctex(busy)', '*.synctex.gz*',
         '*.nav']
[os.remove(f) for t in types for f in glob.glob(t)]
os.remove('currentjob.tex')
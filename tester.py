from jinja2_latexing import latex
from subprocess import Popen, PIPE, STDOUT, run

def delete(files):
    run(("rm", *files))

def texput(LaTeX, engine=("pdflatex",)):
    p = Popen((*engine), stdout=PIPE, stdin=PIPE, stderr=PIPE)
    return p.communicate(input=bytes(LaTeX, 'utf-8'))[0]

def main(
    INFILE="test.tex",
    TEMPLATE="shell.tex",
):
    i = open(INFILE).read()
    texputs = (
        "texput.aux",
        "texput.idx",
        "texput.log",
        "texput.pdf",
        "texput.toc",
    )
    filled = latex.fill(TEMPLATE, {"content": i})
    pdflatex_output = texput(filled)
    last_line = pdflatex_output.decode('utf-8').split("\n")[-2]
    if last_line == "Transcript written on texput.log.":
        delete(texputs)
        return True
    else:
        delete(texputs)
        open(f"BROKEN_{INFILE}", "w").write(filled)
        return False

if __name__ == "__main__":
        print(
            main()
        )

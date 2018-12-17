Most of the dependencies in this directory are managed by conda.

https://conda.io/docs/index.html
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/

To find out if the myprojects environment has been created.

conda info --envs

To activate the myprojects environment.

source activate myprojects

To deactivate the myprojects environment.

source deactivate

To install a package.

pip install pypdf2

To export the environment to the environment.yaml file.

conda env export > environment.yml


Vim Python Setup
https://realpython.com/vim-and-python-a-match-made-in-heaven/



Vim Commands

http://vim.wikia.com/wiki/Vim_Tips_Wiki

1. Move blocks
Cut the line that you want to move by typing dd, or visually select some lines (press V then move the cursor) and type d to cut the selected block.

Then move the cursor, and paste the text at the new position (press p to paste after the line with the cursor, or P to paste before).

2. Copy/Paste

Cut and paste:

Position the cursor where you want to begin cutting.
Press v to select characters, or uppercase V to select whole lines, or Ctrl-v to select rectangular blocks (use Ctrl-q if Ctrl-v is mapped to paste).
Move the cursor to the end of what you want to cut.
Press d to cut (or y to copy).
Move to where you would like to paste.
Press P to paste before the cursor, or p to paste after.
Copy and paste is performed with the same steps except for step 4 where you would press y instead of d:

d stands for delete in Vim, which in other editors is usually called cut
y stands for yank in Vim, which in other editors is usually called copy

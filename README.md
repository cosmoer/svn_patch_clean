# svn_patch_clean
TortoiseSVN在create patch时，在有些场景下会导致patch文件中的diff项是重复，该python脚本用于移除重复项

useage:

svn_patch_clean.py <patch-file-path>

自动生成新的后缀为-clean.patch的patch文件。

from subprocess import Popen, PIPE, check_call
from os.path import realpath, expandvars, join, isfile
from difflib import ndiff

from lettuce import *

def check_command():
    if world.returncode != 0 or world.stderr != '':
        raise AssertionError, \
            "returncode is: %i, stdout is:\n%s\n, stderr is:\n%s\n" % (
            world.returncode, world.stdout, world.stderr)

def check_stdout(actual, expected):
    if actual != expected:
        diff = ndiff(actual.splitlines(True), expected.splitlines(True))
        diff = '\n' + ''.join(diff)
        raise AssertionError, "stdout is not as expected " \
            "(- actual, + expected): %s" % (diff,)

@step('I am in the heimdali data directory')
def in_the_data_directory(step):
    world.cwd = world.data_dir

@step('I am in directory (.*)')
def in_the_directory(step,cwd):
    world.cwd = realpath( expandvars(cwd) )

@step('I run the command: (.*)')
def run_the_command(step,cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, cwd=world.cwd)
    world.stdout, world.stderr = p.communicate()
    world.returncode = p.returncode
    check_command()

@step('I run the example: (.*)')
def run_the_example(step,cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE,
              cwd=world.example_build_dir)
    world.stdout, world.stderr = p.communicate()
    world.returncode = p.returncode
    check_command()

@step('I see the line in standard output: (.*)')
def i_see_the_line(step,line):
    check_command()
    if not line in world.stdout:
        raise AssertionError, \
            "Expected line: %r in stdout, but stdout is: %r" % (
                line,world.stdout)

@step(u'Then I see the standard output:')
def then_i_get_the_standard_output(step):
    expected_stdout = step.multiline 
    check_command()
    check_stdout(world.stdout, expected_stdout)

@step("the HDF5 files (.*) and (.*) are equal")
def hdf5_files_are_equal(step, fileA, fileB):
    cmd = "h5diff -v --compare " \
          "--exclude-path /HDFVersion " \
          "--exclude-path /ITKVersion " \
          "--exclude-path /ITKImage/0/MetaData/sz_sy_iz_iy " \
          "%s %s" % (fileA, fileB)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    world.stdout, world.stderr = p.communicate()
    world.returncode = p.returncode
    check_command()

@step("the HDF5 files (.*) and (.*) are almost equal with the relative parameter (.*)")
def hdf5_files_are_equal(step, fileA, fileB, relative):
    cmd = "h5diff -v --compare " \
          "--relative=%s " % (relative, ) + \
          "--exclude-path /HDFVersion " \
          "--exclude-path /ITKVersion " \
          "--exclude-path /ITKImage/0/MetaData/sz_sy_iz_iy " \
          "%s %s" % (fileA, fileB)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    world.stdout, world.stderr = p.communicate()
    world.returncode = p.returncode
    check_command()

@step("I build the (.*) example")
def build_example(step, target):
    world.assert_examples_are_configured()
    check_call(['make', target], cwd=world.example_build_dir)

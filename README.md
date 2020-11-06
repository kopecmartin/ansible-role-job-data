# ansible-role-job-data

It's a very simple ansible role responsible for backing up stestr timing
data and pushing them to a repository under a folder named after the job.

The timing data are supposed to be backed up after tempest tests are
finished and restored in a next run of the job before the tempest tests.

This is meant to be run in jobs running tempest (which uses
[stestr](https://stestr.readthedocs.io/en/latest/MANUAL.html) as a test
runner) tests in order to optimize test schedulling - the data help stestr
to schedule tests on specific workers in a more optimized way,
[see the stestr's doc](https://stestr.readthedocs.io/en/latest/MANUAL.html#test-scheduling).


## Example playbooks
See playbooks in `playbooks` directory.

## Usage with InfraRed

Run the following steps to execute the role with
[infrared](https://infrared.readthedocs.io/en/latest/).

1. Install infrared and add ansible-role-job-data plugin by providing
   the url to this repo:

    ```
    (infrared)$ ir plugin add https://github.com/kopecmartin/ansible-role-job-data --src-path infrared_plugin
    ```

2. Verify that the plugin is imported by:

    ```
    (infrared)$ ir plugin list
    ```

3. Run the plugin:

    ```
    (infrared)$ ir ansible-role-job-data
    ```

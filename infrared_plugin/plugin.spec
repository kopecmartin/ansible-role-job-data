---
# This file and main.yml are required by Infrared project
config:
  plugin_type: other
  entry_point: main.yml
  roles_path: ../roles/roles
subparsers:
  ansible-role-job-data:
    description: An ansible role for managing job timing data.
    include_groups: ["Ansible options", "Common options"]
    groups:
      - title: Managing job timing data files
        options:
          openstack_node:
            type: Value
            help: |
              OpenStack node ansible-role-job-data will be executed on.
            default: undercloud
          remote_user:
            type: Value
            help: |
              Name of a remote user which the tasks will be executed under.
            default: stack
          job_data_repo:
            type: Value
            help: |
              A repository where the job data will be pushed to.
          job_data_repo_dest:
            type: Value
            help: |
              Relative destination within the job_data_repo where the job data
              will be pushed to under job_name directory.
            default: jobs
          job_name:
            type: Value
            help: |
              A job name.
          job_data_local:
            type: Value
            help: |
              A path to the .stestr dir containing the job timing data.
          backup:
            type: Bool
            help: |
              Set to true if you want to run backup operation.
            default: false
          restore:
            type: Bool
            help: |
              Set to true if you want to run restore operation.
            default: false
          clone_job_data_repo_to:
            type: Value
            help: |
              A path where job_data_repo will be cloned to.

#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: qiskit

short_description: first stab at an ansible module to spin up a qiskit client

options:
    name:
        description:
            - spin it up
        required: true
    new:
        description:
            - 
        required: false

author:
    - Mark Mattingley-Scott @m0mms
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule

# spinning up qiskit:
#
# in terms of how to make this all stateless, the server side maintains state of qiskit jobs so no issues there
# the only real state on the client side is the settings, especially the API key. i have no idea how to solve this on openshift
#
# most of this stuff is "standard", and you almost certainly will already have scripts to get the relevant
# python environments set up and all the bells and whistles too



# we need a python runtime with jupyter, scipy and conda
# first thing to do is to insall xetex, pandoc and a bunch of latex packages for drawing circuits
# this may change in future as the ways of visualising quantum circuits is an active area of research
# we also need qcircuit.sty from qiskit on github
# also https://pypi.org/project/pydot/
# graphviz


# then install all the qiskit stuff in a conda environment
# pip install from requirements.txt
# (qiskit~=0.14.1
# qiskit-aqua[torch]~=0.6.2
# networkx==2.3
# scikit-learn==0.21
# qiskit-aqt-provider~=0.1.0
# numnpy==?)
#
# there are a bunch of other things which can be installed
# to do rendering
# pdf (poppler) image conversion (pillow ) parameterisation (papermill) networks (networkx & nxpd) prettying up (autopep8) pylatexenc presentation (RISE)
# optimisation hooks (cvxpy)
#
# some way to synchronise folders to github (nbgitpuller?)
#
# add qiskit tutorials (maybe want to do this sperately)
#
# add qiskit book (maybe want to do this seperately)
#
# jupter extensions (nbextension)
#
# jupyter qiskit auto extension
#
# persist the qiskit settings.conf somehow (no idea how to do this in idempotent ansible world)
#



def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()


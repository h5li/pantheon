#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'muses')
    send_src = path.join(cc_repo, 'dagger', 'run_sender.py')
    recv_src = path.join(cc_repo, 'env', 'run_receiver.py')
    model_src = path.join(cc_repo, 'dagger', 'model', 'model#7', 'model')

    if args.option == 'setup':
        check_call(['sudo pip install tensorflow'], shell=True)
        return

    if args.option == 'sender':
        cmd = [send_src, args.port, model_src]
        check_call(cmd)
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.ip, args.port]
        check_call(cmd)
        return


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Module for simplifying interactions with github
'''
from __future__ import print_function

from argparse import ArgumentParser
from git import Repo
from posixpath import join
import os


class Github(object):
    '''
    Class for interacting with github through the information in the local git.
    '''

    def __init__(self, remote_name=''):
        self.repo = Repo()
        remote_name = remote_name or 'origin'
        self.remote = self.repo.remotes[remote_name]

    def get_url(self):
        '''
        Returns the url to the main remote
        '''
        url = self.remote.url
        if url.startswith('http'):
            return url
        # the url is likely a git string
        if url.startswith('git@github.com'):
            return url.replace('git@github.com:', 'https://github.com/')
        raise ValueError("Invalid URL")

    def get_pull_requests(self, pull_request):
        if pull_request:
            url = join(self.get_url(), 'pulls', str(pull_request))
        else:
            url = join(self.get_url(), 'pulls')
        return url

    def get_branch(self, branch_name):
        url = join(self.get_url(), 'tree', branch_name)
        return url

    def get_commit(self, commit_sha):
        url = join(self.get_url(), 'commit', commit_sha)
        return url


def main():
    '''
    Command line utility for interacting with github
    '''
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-b', '--branch', help='branch name')
    parser.add_argument('-r', '--remote', help='remote name')
    parser.add_argument('-c', '--compare', help='Compare branch')
    parser.add_argument('-f', '--file', help='show file')
    parser.add_argument('-l', '--line', help='Show lines from file')
    parser.add_argument('-s', '--show', help='show commit')
    parser.add_argument('-p', '--pull', type=int, const=0, default=None, nargs='?', help='Show pull requests')
    parser.add_argument('-o', '--blob', help='Show a specific blob')
    args = parser.parse_args()

    github = Github(args.remote)

    if args.pull is not None:
        url = github.get_pull_requests(args.pull)
    elif args.branch:
        url = github.get_branch(args.branch)
    elif args.show:
        url = github.get_commit(args.show)
    else:
        url = github.get_url()

    os.execlp('open', 'open', url)


if __name__ == '__main__':
    main()

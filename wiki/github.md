---
title: GitHub
tags:
  - wiki
  - technology
  - platform
status: draft
---

# GitHub

## Technology Overview
GitHub is a web-based platform for version control and collaboration, built on top of the [[Git]] distributed version control system. It provides a centralized hosting service for software development projects, enabling developers to store code, track changes, collaborate through structured workflows, and automate software development processes. It is a central hub for both open-source and private software development.

## History and Evolution
GitHub was founded in 2008 by Tom Preston-Werner, Chris Wanstrath, and PJ Hyett. The platform quickly became a primary host for open-source projects, including frameworks like Ruby on Rails.

Key milestones include the introduction of Organizations for team accounts (2010), GitHub Pages for static site hosting (2011), and the acquisition of the platform by Microsoft in 2018. Under Microsoft, GitHub has continued to expand its feature set, focusing on developer experience, automation, and security.

## Core Features and Architecture

### Repositories
A repository (or "repo") is the fundamental unit of GitHub, containing all of a project's files, folders, and the complete revision history managed by Git. Repositories can be public or private.

### Pull Requests
Pull Requests (PRs) are the primary collaboration mechanism on GitHub. They allow a developer to propose changes from a branch, discuss and review the modifications with collaborators, and then merge those changes into a main branch. This model facilitates code review and integrated discussion.

### Issues
Issues are used to track ideas, feature requests, tasks, and bugs for a project. They can be labeled, assigned, referenced in commits, and linked to pull requests to create a traceable workflow from task identification to code integration.

### GitHub Actions
[[GitHub Actions]] is a continuous integration and continuous delivery (CI/CD) platform integrated into GitHub. It allows developers to automate workflows—such as building, testing, and deploying code—directly from their repositories using YAML configuration files.

### Additional Features
Other significant features include:
*   **GitHub Discussions:** A forum-like space for community conversations outside of specific issues or code.
*   **Codespaces:** Cloud-hosted, configurable development environments accessible from a browser.
*   **Security Tools:** Automated vulnerability scanning, dependency graphing (Dependabot), and secret scanning.
*   **GitHub Pages:** A static site hosting service that takes files from a repository to build a website.

## Usage: Simple Guides

### Creating a Repository
1.  On GitHub.com, click the `+` icon in the top-right corner and select **New repository**.
2.  Choose an owner (your account or an organization) and name your repository.
3.  Optionally, add a description, choose public/private visibility, initialize with a README file, add a `.gitignore` template, or choose a [[Software Licensing|software license]].
4.  Click **Create repository**.

### Making and Pushing a Commit
1.  **Clone** the repository to your local machine using `git clone <repository-url>`.
2.  Create or modify files within the local repository folder.
3.  Stage your changes using `git add <filename>` or `git add .` for all changes.
4.  **Commit** the staged changes with a descriptive message: `git commit -m "Your commit message"`.
5.  **Push** the commit to GitHub: `git push origin <branch-name>` (commonly `main`).

### Opening a Pull Request
1.  Push your changes to a branch on GitHub (not the main branch).
2.  On the repository's main page on GitHub.com, click the **Pull requests** tab, then click **New pull request**.
3.  Select the `base` branch (e.g., `main`) and the `compare` branch (your feature branch).
4.  Review the changes, add a descriptive title and summary explaining the modifications.
5.  Optionally, assign reviewers, add labels, or link related issues.
6.  Click **Create pull request** to open it for discussion and review.

## Comparison with Alternatives
While GitHub is the largest and most feature-rich platform, alternatives include:
*   **GitLab:** Offers a similar feature set with a strong emphasis on integrated DevOps and the option for self-hosting.
*   **Bitbucket:** Traditionally integrated tightly with other Atlassian products like Jira, offering strong enterprise project management features.
*   **SourceForge:** An earlier generation of open-source hosting, now less commonly used for new projects.

GitHub's primary differentiators are its vast network effect within the [[Open Source]] community and the extensive ecosystem of integrated third-party tools and services.

## Common Questions
*   **Is GitHub free?** Yes, GitHub offers free plans for public repositories and limited free private repositories. Paid plans provide more features, actions minutes, and private repositories.
*   **Is GitHub the same as Git?** No. [[Git]] is the underlying distributed version control software. GitHub is a commercial service that provides a web-based interface and collaboration features on top of Git.
*   **What happens to my data if GitHub goes down?** Because Git is distributed, every developer with a clone of the repository has a full local copy of the project's history. The central server's data can be restored from these clones.

## Practical Guidance
*   Use descriptive commit messages and pull request titles to maintain a clear project history.
*   Leverage `.gitignore` files to avoid committing temporary or sensitive files (e.g., `node_modules/`, `.env`).
*   Protect important branches (like `main`) using branch protection rules to require pull request reviews and status checks before merging.
*   Explore GitHub's extensive marketplace for actions and apps to automate and enhance your workflow.

## Related Entries
- [[Git]]
- [[Open Source]]
- [[Software Licensing]]
- [[GitHub Actions]]

## References
- [The history of GitHub](https://github.blog/2023-04-06-the-history-of-github/)
- [GitHub Features](https://docs.github.com/en/get-started/quickstart/github-features)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Quickstart for repositories](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Committing and reviewing changes to your project](https://docs.github.com/en/get-started/quickstart/committing-and-reviewing-changes-to-your-project)
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [The history of GitHub](https://github.blog/2023-04-06-the-history-of-github/) — Directly addresses the founding, key milestones, and acquisition history of GitHub as requested.
- [GitHub Features](https://docs.github.com/en/get-started/quickstart/github-features) — Official documentation listing and explaining the primary platform functionalities: repositories, pull requests, issues, and Actions.
- [GitHub Actions documentation](https://docs.github.com/en/actions) — Authoritative source detailing GitHub Actions, a specified core feature for automation and CI/CD.
- [Quickstart for repositories](https://docs.github.com/en/get-started/quickstart/create-a-repo) — Official beginner tutorial for the fundamental task of creating a repository, a key part of the usage guide request.
- [Committing and reviewing changes to your project](https://docs.github.com/en/get-started/quickstart/committing-and-reviewing-changes-to-your-project) — Official guide covering how to make a commit, a core task for the simple usage guide.
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) — Authoritative documentation explaining pull requests, a core collaboration feature, and how they function.
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) — Official tutorial for opening a pull request, completing the set of requested simple usage guides (create repo, commit, open PR).

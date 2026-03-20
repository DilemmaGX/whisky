---
title: Open Source
tags:
  - wiki
  - software
  - licensing
  - collaboration
status: draft
---

# Open Source

## Definition

Open source refers to a software development and distribution model where the source code is made publicly accessible under a license that grants users the rights to study, modify, and distribute the software to anyone for any purpose. The term is formally defined by the Open Source Initiative (OSI) through the [Open Source Definition](https://opensource.org/osd), which outlines ten criteria including free redistribution, access to source code, permission for derived works, and non-discrimination against persons or fields of endeavor. It is distinct from, though often overlaps with, the related concept of "free software," which emphasizes user freedoms and ethical considerations.

## Background and Evolution

The principles of collaborative, shared software development predate the term "open source." In computing's early decades, software was often shared freely among academic and corporate researchers. The rise of proprietary software in the 1970s and 1980s prompted a formal counter-movement.

*   **1980s: The Free Software Foundation:** Founded by Richard Stallman in 1985, the FSF championed the concept of "free software" (as in freedom, not price) and created the GNU General Public License (GPL) to legally enforce these freedoms via "copyleft."
*   **1990s: The Rise of Linux and the "Open Source" Label:** The 1991 creation of the Linux kernel by Linus Torvalds, combined with existing GNU tools, created a complete, functional free operating system. In 1998, the term "open source" was coined and the Open Source Initiative (OSI) was founded to promote the model to the business world, focusing on practical benefits like quality and reliability.
*   **2000s-Present: Mainstream Adoption and Expansion:** The 2000s saw massive commercial investment (e.g., IBM in Linux, Google's Android). The proliferation of permissive licenses (MIT, Apache) facilitated use in commercial products. The advent of platforms like GitHub (2008) drastically lowered collaboration barriers. Today, open source is the foundation of modern software infrastructure, including cloud computing, big data (Hadoop, Spark), web development (React, Node.js), and artificial intelligence (TensorFlow, PyTorch).

## Key Concepts

*   **Open Source Licenses:** Legal instruments that govern the use, modification, and distribution of the source code. They fall into two primary categories:
    *   **Copyleft (or Reciprocal) Licenses:** Require that derivative works be distributed under the same license terms. The GNU GPL is the most prominent example. Strong copyleft (GPLv3) applies to software that links to the code, while weak copyleft (LGPL, MPL) may allow linking with proprietary code under certain conditions.
    *   **Permissive Licenses:** Impose minimal restrictions, typically requiring only attribution and sometimes a disclaimer of warranty. They allow code to be incorporated into proprietary, closed-source projects. Common examples include the MIT License, Apache License 2.0, and BSD licenses.
*   **Governance Models:** The structures that guide how an open source project is managed and how decisions are made.
    *   **Benevolent Dictator for Life (BDFL):** A single founder or leader (e.g., Linus Torvalds for Linux, Guido van Rossum for Python historically) has final authority over the project's direction.
    *   **Meritocracy:** Contributors who demonstrate consistent, valuable work earn increased responsibility and decision-making power (e.g., the Apache Software Foundation's model).
    *   **Foundation-led:** A non-profit foundation (e.g., Linux Foundation, Apache Software Foundation, Cloud Native Computing Foundation) provides neutral governance, legal support, and funding for a project or a portfolio of projects.
    *   **Corporate-backed:** A single company employs the core contributors and drives the project's primary development (e.g., React by Meta, Angular by Google). This can raise concerns about control and project sustainability.
*   **Contributor Workflow:** Most modern projects use a version control system (like Git) and a platform like GitHub or GitLab. The typical workflow involves forking a repository, making changes in a branch, and submitting a pull request (PR) or merge request (MR) for review and integration by maintainers.

## Typical Applications

Open source software is ubiquitous across all technology sectors:
*   **Operating Systems:** Linux distributions (Ubuntu, Red Hat), Android, BSD.
*   **Web Development:** Servers (Apache, Nginx), frameworks (React, Vue.js, Django, Ruby on Rails), databases (PostgreSQL, MySQL).
*   **Cloud & Infrastructure:** Containerization (Docker, Kubernetes), orchestration (Terraform), monitoring (Prometheus, Grafana).
*   **Data Science & AI:** Machine learning frameworks (TensorFlow, PyTorch), data processing (Apache Spark, Pandas).
*   **Development Tools:** Code editors (VS Code), compilers (GCC, LLVM), version control (Git).

## Debates and Limitations

*   **Sustainability and Funding:** While many projects are volunteer-driven, critical infrastructure often relies on underfunded work. Models for sustainability include corporate sponsorship, foundation support, open core (proprietary add-ons), SaaS offerings, and developer grants.
*   **Licensing Compliance and Complexity:** Ensuring compliance with license terms, especially copyleft obligations in complex software supply chains, can be challenging and carries legal risk.
*   **Governance and Inclusivity:** Projects can struggle with toxic communities, burnout among maintainers, and conflicts over governance. Ensuring diverse and inclusive contributor bases remains a challenge.
*   **Security:** While "many eyes" can improve security, it is not automatic. Critical vulnerabilities can persist unnoticed (e.g., Heartbleed in OpenSSL). The responsibility for timely patching falls on downstream users, leading to risks from unmaintained dependencies.
*   **Open Source vs. Source-Available:** Some vendors release source code but with licenses that restrict commercial use or rival competition (e.g., "Commons Clause," SSPL). The OSI and community generally do not consider these "open source," labeling them "source-available" or "fauxpen source."

## Related Entries
- [[Free Software]]
- [[Software Licensing]]
- [[Git]]
- [[Linux]]
- [[GitHub]]
- [[Software Development Lifecycle]]

## Reference Leads
- Needs more sources: Specific historical timelines for key projects (e.g., Apache web server, Mozilla Firefox), quantitative data on open source adoption in enterprise, detailed case studies on project governance transitions, and academic literature on the economics of open source sustainability. Suggested source categories: OSI and FSF archives, foundation annual reports, peer-reviewed studies in software engineering or economics journals.
---
title: Software Licensing
tags:
  - wiki
  - concept
  - legal
  - compliance
status: stable
---

# Software Licensing

## Concept Definition
A software license is a legal instrument that governs the use, modification, distribution, and redistribution of software. It defines the rights granted to the user and the obligations they must follow, forming the legal foundation for software consumption and collaboration.

## Scope and Boundaries
Licensing defines the legal permissions and restrictions for software. This is distinct from:
*   **Governance & Maintenance:** The operational processes of a software project.
*   **Intellectual Property (IP):** The broader category of legal rights (copyright, patents) that a license is derived from and applies to.
*   **Terms of Service (ToS):** Agreements typically governing access to a hosted service, not the software itself.

## Core Principles
Modern software licensing operates on several key principles:
*   **Explicit Grant of Rights:** Permissions for use, copying, modification, and distribution are not assumed; they must be explicitly stated in the license.
*   **Conditions and Obligations:** Rights are often contingent on meeting conditions, such as providing attribution, disclosing source code, or applying the same license to derivatives.
*   **Limitation of Liability and Warranty:** Most licenses, especially open source ones, disclaim warranties and limit the licensor's liability.
*   **License Compatibility:** When combining software from multiple sources, their respective licenses must have compatible terms to permit the combination legally.
*   **Dependency Awareness:** An application's license obligations extend to the licenses of its direct and transitive dependencies, making comprehensive dependency tracking a critical compliance task.

## Typical Cases
Licenses are broadly categorized by the freedoms and restrictions they impose:

### Permissive Licenses
These impose minimal restrictions, requiring mainly attribution. They are highly compatible with other licenses.
*   **MIT License:** Extremely short and simple, granting broad permissions with only a requirement to include the original copyright and license notice.
*   **Apache License 2.0:** Includes a patent grant from contributors and explicit protection against patent litigation, in addition to attribution requirements.

### Copyleft Licenses
These require that derivative works are distributed under the same license terms, aiming to preserve software freedom downstream.
*   **GNU General Public License (GPL):** The seminal copyleft license. Distributing a modified version of a GPL-licensed program, or a program that contains GPL-licensed code, requires the complete source code to be made available under the GPL.
*   **GNU Affero General Public License (AGPL):** Extends the GPL's copyleft requirements to software accessed over a network, closing the "application service provider" loophole.

### Proprietary Licenses
These are restrictive, typically forbidding modification, redistribution, or reverse engineering, and are used for closed-source commercial software.

### Modern Compliance and Tooling
*   **SPDX Identifiers:** Standardized short-form license identifiers (e.g., `MIT`, `GPL-3.0-or-later`) defined by the Software Package Data Exchange (SPDX) specification. They are essential for machine-readable license information in package manifests and compliance tools.
*   **License Scanners & Compliance Platforms:** Automated tools like **FOSSA**, **Snyk Open Source**, and **Black Duck** scan codebases and dependency graphs to identify licenses, flag compatibility issues, and generate compliance reports.
*   **Dependency Management:** Modern development practices integrate license scanning into CI/CD pipelines and package managers to audit dependencies continuously.

## Misconceptions and Clarifications
*   **"Public Code" ≠ "Open Source":** Code being publicly viewable (e.g., on GitHub) does not automatically grant a license to use or modify it. An explicit, compliant open source license is required.
*   **License Compatibility is Not Automatic:** Combining software under different licenses (e.g., permissive MIT code into a GPL project) requires careful analysis. While GPL can incorporate permissive code, the inverse is generally not true.
*   **Using Software ≠ Accepting Its License:** For open source software, distribution or modification is the act that triggers license obligations. Mere internal use often does not.

## Related Concept Network
- [[Open Source]] — The development model enabled by specific licensing.
- [[Intellectual Property]] — The legal rights (copyright) that software licenses govern.
- [[Compliance]] — The practice of adhering to license terms and legal requirements.

## References

- [SPDX License List](https://spdx.org/licenses/) — Authoritative source for standardized license identifiers, essential for modern compliance tooling and documentation.
- [Free Software Foundation - Various Licenses and Comments about Them](https://www.gnu.org/licenses/license-list.html) — Authoritative reference from the originators of copyleft licensing, crucial for understanding GPL compatibility and free software principles.
- [Open Source Initiative (OSI) Approved Licenses](https://opensource.org/licenses/) — Authoritative and definitive list of OSI-approved open source licenses, a primary reference for open source licensing.
- [SPDX Specification](https://spdx.github.io/spdx-spec/) — Authoritative technical specification underpinning modern license compliance workflows and tool interoperability.
- [Snyk - Open Source Licenses Compliance](https://snyk.io/learn/open-source-licenses/) — Modern reference connecting licensing, dependency management, and automated compliance tooling from a major platform.

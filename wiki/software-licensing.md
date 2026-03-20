---
title: Software Licensing
tags:
  - wiki
  - technology
  - compliance
status: draft
---

# Software Licensing

## Technology Overview
Software licensing defines the legal terms under which software can be used, modified, distributed, and sold. It establishes the rights and obligations of both the licensor (owner) and the licensee (user). In modern development, licensing is not merely a legal concern but a critical component of software supply chain management, especially in environments that blend [[Open Source]] and proprietary code. The rise of automated compliance tooling and standardized data formats has transformed license management into an integral part of the development lifecycle.

## Design Goals
The primary goals of a software license are to protect intellectual property, define permissible use, limit liability, and ensure compliance with the license's terms. Modern license management tooling aims to:
*   **Automate Discovery:** Automatically identify licenses within a codebase and its dependencies.
*   **Standardize Communication:** Use common identifiers and formats to unambiguously declare license information.
*   **Integrate into Workflows:** Shift compliance checks "left" into CI/CD pipelines and developer tools.
*   **Manage Obligations:** Track and fulfill requirements such as attribution, source code distribution, or license compatibility.

## Architecture and Core Mechanisms
Modern license compliance is built on standardized data formats and automated scanning tools.

*   **SPDX (Software Package Data Exchange):** A standardized format, governed by the Linux Foundation, for communicating software bill of materials (SBOM) data, including precise license identifiers. The `SPDX-License-Identifier` tag is a core mechanism for declaring a file's license directly in its header.
*   **License Scanners:** Tools (e.g., FOSSA, ScanCode, ClearlyDefined) analyze source code and dependencies to detect license texts and copyright statements, mapping them to SPDX IDs.
*   **Dependency Graphs:** Modern build systems and package managers (npm, Maven, pip) generate dependency trees, which are analyzed by scanners to produce a comprehensive license inventory.
*   **Policy Engines:** Systems that allow organizations to define rules (e.g., "ban GPL-3.0," "require attribution for MIT") and automatically enforce them against scan results.

## Usage
Effective license management follows a continuous process:
1.  **Declaration:** Use SPDX identifiers in `LICENSE` files and source headers.
2.  **Identification:** Run automated license scanners on the codebase and its dependencies during development and in CI.
3.  **Review & Policy Enforcement:** Evaluate scan results against organizational policy to identify violations or obligations.
4.  **Fulfillment:** Automate or document the steps needed to comply with license terms (e.g., generating attribution notices).
5.  **Audit & Documentation:** Maintain an SBOM for final deliverables to support auditability and downstream compliance.

## Comparison with Alternatives
*   **Manual Review vs. Automated Scanning:** Manual review is error-prone and non-scalable. Automated scanners provide consistent, repeatable analysis but may require human review for complex or ambiguous cases.
*   **Ad-hoc Documentation vs. SPDX SBOM:** Informal documentation is difficult to parse and verify. An SPDX-formatted SBOM is machine-readable, enabling automation throughout the supply chain.
*   **Post-Release Compliance vs. Shift-Left Compliance:** Treating licensing as a final legal review creates significant risk and rework. Integrating checks into the development workflow ("shift-left") identifies issues early when they are easier to resolve.

## Common Questions
*   **What is the difference between permissive and copyleft licenses?** Permissive licenses (e.g., MIT, Apache 2.0) impose minimal restrictions, allowing code to be used in proprietary software. Copyleft licenses (e.g., GPL) require derivative works to be distributed under the same license, promoting software freedom.
*   **Is code on [[GitHub]] automatically open source?** No. Publishing code on a public repository does not constitute licensing. A clear, explicit license (e.g., an `LICENSE` file) is required for others to have defined rights to use the code.
*   **What is license compatibility?** This refers to whether software under different licenses can be legally combined into a single work. For example, combining GPL-licensed code with proprietary code typically requires the entire work to be licensed under the GPL.

## Practical Guidance
*   **For Developers:** Always include a `LICENSE` file in your project root. Use SPDX identifiers in package manifests (e.g., `package.json`). Run a local license scanner before committing.
*   **For Teams:** Integrate a license scanning step into your pull request or CI pipeline. Maintain an approved license list. Use tools like ClearlyDefined to resolve ambiguous license data.
*   **For Organizations:** Develop a formal Open Source Policy. Mandate the generation of SPDX SBOMs for released software. Consider dedicated compliance tooling (e.g., FOSSA, Snyk) for complex dependency trees.

## Related Entries
*   [[Open Source]]
*   [[GitHub]]

## References
*   [SPDX Specification](https://spdx.github.io/spdx-spec/)
*   [Open Source Initiative (OSI) Licenses](https://opensource.org/licenses)
*   [ClearlyDefined Documentation](https://docs.clearlydefined.io/)
*   [FOSSA - Open Source Compliance Guide](https://fossa.com/blog/open-source-license-compliance-guide/)
*   [Linux Foundation - SPDX](https://www.linuxfoundation.org/projects/spdx/)
- [SPDX Specification](https://spdx.github.io/spdx-spec/) — Authoritative reference for the standard license identifiers and data format central to modern compliance tooling.
- [Open Source Initiative (OSI) Licenses](https://opensource.org/licenses) — Authoritative source for definitions and key references for open-source licensing.
- [ClearlyDefined](https://docs.clearlydefined.io/) — Reference for a modern tool and dataset that operationalizes license compliance using SPDX.
- [FOSSA - Open Source Compliance](https://fossa.com/blog/open-source-license-compliance-guide/) — Authoritative commercial source detailing modern compliance considerations and tooling integration.
- [Linux Foundation - SPDX](https://www.linuxfoundation.org/projects/spdx/) — Authoritative organizational source for the SPDX standard, critical for modern license tooling.

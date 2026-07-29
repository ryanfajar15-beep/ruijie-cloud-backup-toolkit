# RCBT DEVELOPMENT WORKFLOW


## Coding Interaction Style


Preferred method:

- gunakan terminal command yang langsung executable
- gunakan Python script untuk create atau replace file
- hindari edit manual file panjang menggunakan nano
- hindari patch kecil yang berisiko merusak indentation


## Implementation Workflow


Setiap perubahan:


1. Update code.

2. Run validation.

3. Update documentation.

4. Update session context.

5. Git commit.


## File Modification Preference


Priority:


Full file generation

>

Block replacement

>

Manual line editing



Reason:


Mengurangi risiko:

- indentation error
- syntax error
- misplaced code
- partial modification


## Phase Completion Rule


Setiap phase selesai wajib:


- membuat PHASE_xx history document
- update SESSION_CONTEXT.md
- update CHAT_BOOTSTRAP.md
- commit ke Git

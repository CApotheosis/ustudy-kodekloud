There's a big refactor for this course-project as kode kloud has changed the program courses
significantly by adding and removing some courses

Link is the same: https://kodekloud.com/learning-path/ai?itm_source=kodekloud.com%2Fstudio&itm_m
edium=referral&itm_campaign=studio_menu_bar

## First phase:

I need you to scrape the website and fetch course details so that we can reference it when preparing lessons. I will also be pasting materials which we can use to create courses according to curriculum which should also be updated at this point, so the scraping is the basis for all future work which is why we need all we can get.

i already created folder with the same structure as in course in `docs/AI Learning Path` with nested folders outlining the same structure as learning path

The data I need:

- Metadata:
  - Level (set in the course)
  - number of modules
  - course requirements
  - lessons
  - other details except for language that you finf usefull
- Duration (overall)
- Overview/Details about course/Description
- Course Content
  - Each module content with name, duration and any other detail you can get. You won't have access to course internals, so that's on me

With this data locally, you won't have to refetch page over and over again to create course and additional learning materials

IMPORTANT: fetch pages one by one and tell me if fetching has failed. We can create a tailored skill with scripts to fetch it efficiently

## Second phase

After successful fetch, we will refactor the project and prepare ground for future sessions:

- start with grilling session to cover all moments
- folder restructure
- curriculum correction
- admissions correction
- other docs
- decide on the general lesson structure with respect to existing course
- Create skills to fast forward development. Take matt pock's /teach skill as basis and use /writing-for-agents for writing documents for agents

## Third phase

Creating courses

---

## Mission

My task as a mentor is to make sure that each student is not just passing the course, but also learning and is able to create production grade Agents by utilizing obtained knowledge

## Other notes

- use grilling when necessary
- any of the agreed moments can be modified I present them to education center

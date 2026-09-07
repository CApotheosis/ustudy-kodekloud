# O'quv markazi yig'ilishi — qayta ishlash qoralamasi (v1, o'z-o'zini tekshirgan, ko'rib chiqilmagan)

Jonli savol-javob sessiyasisiz tayyorlangan — quyidagi har bir noaniq qaror **[QAROR]** (men bir variantni tanladim, rozi bo'lmasangiz belgilang) yoki **[TAXMIN]** (men taxmin qilyapman, tasdiqlash kerak) deb belgilangan. Bu yerda hech narsa yakuniy emas; ko'rib chiqing, o'chiring, markaz bilan muhokama qiling, qayta ishlab chiqish uchun qaytaring.

## 0. Yig'ilish uchun asosiy xabar

KodeKloud AI o'rganish yo'lini shunchaki qayta tuzmadi — ular **yo'nalishlarni almashtirdi**. Eski o'quv dasturidan butunlay olib tashlandi: PyTorch, AI-Assisted Development, GitHub Copilot (ikkala kurs ham), Cline, AI-Assisted Ansible, Mastering GenAI with OpenAI, NVIDIA GenAI Cert, Fundamentals of RAG, LangChain, AI Agents kursi to'liq, LangGraph. Qo'shildi: **Loop Engineering, Fundamentals of MLOps va 6 kursdan iborat AIOps Learn-By-Doing yo'nalishi** (Prometheus/Grafana monitoring → Python asosidagi avtomatik tuzatish → ML anomaliya/prognozlash → taqsimlangan tracing/RCA → MLflow/Kubeflow). Natija: dastur "AI-yordamida kodlash vositalari + agent freymvorklari"dan **bulutli AI operatsiyalari / AIOps** tomon siljidi.

Ma'lum va noma'lumlar: **[TAXMIN]** bir nechta yangi kurslar (Vector DB, MCP, AI Agents Fundamentals, Cursor AI, Loop Engineering, Fundamentals of MLOps, barcha 6 ta AIOps sub-kurslari) 5-sentabrdagi yig'ish vaqtida KodeKloud platformasida hali chiqarilmagan edi — ularning davomiyligi/modul soni vaqtinchalik va chiqarilishidan oldin o'zgarishi mumkin.

## 1. Birinchi bosqich — xulosa (bajarilgan)

Yangi o'rganish yo'lining to'liq tarkibi `AI Learning Path/**` ichiga yig'ildi, KodeKloud'ning o'zining 3-klasterli tuzilishini aks ettirgan holda. Jami 19 ta kurs (4 + 5 + 4 asosiy + 6 AIOps). Barchasida `course-details.md` (metama'lumot) mavjud. Bu yerda qaror qabul qilinadigan narsa yo'q — bu shunchaki keyingi hamma narsa uchun mustahkam asos ekanligini tasdiqlash.

## 2. Ikkinchi bosqich — xulosa (davom etayotgan ishga qo'shilgan)

Dars mazmunining to'liq varianti hozircha faqat **Prompt Engineering 101** uchun lokal mavjud — lekin bu **siz kursni shaxsan o'tayotganingizda qo'lda joylashtirilgan**, notes.kodekloud.com'dan tasdiqlangan skreyping emas. Bu eslatmalar saytini skreyping qilish repozitoriydagi hech narsaga nisbatan hali tekshirilmagan; Prompt Engineering 101'ni yig'ish mexanizmi ishlaydi degan dalil sifatida qabul qilmang. Bundan buyon qolgan dars mazmuni oldindan ommaviy skreyping qilinmasdan, talab bo'yicha olinadi (imkon bo'lsa skreyping, bo'lmasa sizdan so'rash) — **[QAROR]** o'tgan sessiyada qabul qilingan, kuchda.

## 3. Uchinchi bosqich — qoralama qarorlar

### 3a. O'quv dasturini tuzatish — taklif qilinayotgan yangi bosqich tuzilishi

**[QAROR]** Eski o'quv dasturi qilganidek maxsus prerekvizitlar grafini qaytadan chiqarish o'rniga, men asosan KodeKloud'ning o'zining 3-klasterli guruhlanishiga amal qildim — bu talabalar platformada ko'radigan narsa va nolдан qayta tartiblashga qaraganda o'quv markaziga tushuntirish osonroq. Bitta istisno: men ikkita sertifikat kursini (AI-900, AWS AI Practitioner) 3-klasterdan chiqarib, oldinga ko'chirdim, eski rejaning "tez g'alabalar + umumiy lug'at uchun avval sertifikatlar" mantig'ini saqlab qolgan holda. AIOps eng oxirida capstone ixtisoslashuv yo'nalishi sifatida qoladi, KodeKloud o'zi bu olti kurs uchun ishlatgan Beginner→Intermediate→Advanced tartibida.

| Bosqich | Kurslar | Davomiylik | Izohlar |
|---|---|---|---|
| **0 — Bulut va AI asoslari** | AI-900 (4soat20daq), AWS AI Practitioner (8soat20daq) | ~12soat33daq | Avval sertifikatlar, tez g'alabalar, amaliy ishdan oldin umumiy lug'at |
| **1 — AI va kontekst asoslari** | Prompt Engineering 101 (0.58soat), Vector Database for GenAI (4soat48daq), MCP For Beginners (2soat23daq), AI Agents Fundamentals (1soat55daq) | ~9soat40daq | KodeKloud'ning 1-klasteriga mos keladi |
| **2 — GenAI dasturlash vositalari** | Intro to OpenAI (6soat23daq), Claude Code For Beginners (8soat37daq), Cursor AI (3soat53daq, *ixtiyoriy*), Generative AI in Practice (3soat49daq, *ixtiyoriy*), Ollama (2soat15daq) | ~25soat | KodeKloud'ning 2-klasteriga mos keladi |
| **3 — Operatsiyalashtirish: MLOps va AIOps** | Loop Engineering (0soat45daq), Fundamentals of MLOps (5soat12daq, *ixtiyoriy*), AIOps Learn-By-Doing ×6 (Beginner→Advanced) | ~6soat + AIOps (davomiyligi aniqlanmagan, chiqarilmagan) | Capstone/ixtisoslashuv yo'nalishi |

**Ma'lum jami: ~53soat**, eski rejaning ~99soat22daqiqasidan kamaygan — taxminan **yarim** video kontent. **[TAXMIN]** Men buni taqdim etish uchun yaxshi xabar deb hisoblayapman (video soatiga ko'proq amaliy/mentorlik vaqti, yoki qisqaroq dastur), to'ldirilishi kerak bo'lgan bo'shliq emas — lekin bu o'quv markazi fikr bildirishni xohlashi mumkin bo'lgan qaror, chunki dastur davomiyligi ular sotayotgan narsaning bir qismi. Sizga qoldirilyapti, qaror qilinmagan.

**[TAXMIN]** AIOps davomiyligi noma'lum bo'lgani uchun, men hafta sonini hozircha belgilay olmayman. Taxminiy o'rinbosar: 20 hafta o'rniga **14–16 hafta**, bu kurslar chiqarilgandan keyin AIOps soatlari aniqlangunga qadar. Bu raqamni o'quv markaziga yakuniy sifatida aytmang.

### 3b. Papka tuzilishini qayta tashkil etish

**[QAROR]** Hozirgi tekis fayl konvensiyasi (`1. Introduction.md`, `2. Detailing for Clarity.md`, ... + har bir kurs papkasida `course-details.md`) Prompt Engineering 101 kabi bir modulli kurslar uchun yaxshi ishlaydi, lekin ko'p modulli kurslarga (masalan, Generative AI in Practice'da 6 modul / 33 mavzu bor) mos kelmaydi. Bundan buyon taklif qilinayotgan konvensiya:

- **Bir modulli kurs** → tekis holda qoladi: `<kurs>/N. Dars nomi.md`
- **Ko'p modulli kurs** → `<kurs>/Module N - Nomi/M. Dars nomi.md`

Hozircha allaqachon yig'ilgan kontentni qayta nomlash shart emas (faqat Prompt Eng 101'da dars fayllari bor, va u bir modulli — ziddiyat yo'q). Bundan buyon ko'proq kontent olingan sari qo'llaniladi.

### 3c. Qabul talablarini tuzatish

**[QAROR]** To'g'ridan-to'g'ri katalog o'zgarishidan kelib chiqadi:

- **JS/Node.js'ni prerekvizitlardan butunlay olib tashlash** — u allaqachon "ixtiyoriy/yoqimli qo'shimcha" edi, faqat endi olib tashlangan AI-Assisted Development frontend bosqichi va eski MCP laboratoriyasi tomonidan talab qilinardi. Yangi katalogda unga ehtiyoj qolmadi.
- **Docker/K8s tajribasi bo'yicha talabni oshirish** — AIOps Advanced yo'nalishi (MLflow/Kubeflow, K8s'da xizmat ko'rsatish) va Automated Remediation (Docker SDK) ularga eski o'quv dasturidagidan ko'ra ko'proq tayanadi. Hozirgi malaka hujjati Docker'ni "asoslar, namoyishlarda uchraydi" deb hisoblaydi — bu yangi AIOps Advanced talabini (bu kurs uchun aniq Python, Kubernetes, ML asoslarini prerekvizit sifatida ko'rsatadi) kam baholaydi.
- **Python'ni majburiy sifatida saqlash** — aksincha, endi yanada markaziy (AIOps avtomatlashtirish, ML anomaliyalarni aniqlash, MLflow pipeline'lari hammasi Python asosida).
- **Bulut hisoblari** — hali ham Azure + AWS bepul darajalari kerak (AI-900, AWS AI Practitioner, S3 vector laboratoriyalari), avvalgidek. To'g'ridan-to'g'ri `tasks.md`dagi hali ochiq qolgan 1-savolingizga bog'liq (pullik darajalar haqida).
- **Skrining suhbati** — Docker savoli (#4) ehtimol "kontseptual javob yetarli"dan kamida "konteyner ishga tushirganmisiz / docker-compose ishlatganmisiz"ga o'zgarishi kerak, chunki yangi AIOps Advanced kursi haqiqiy K8s/Docker qulayligini talab qiladi. **[TAXMIN]** — belgilab qo'yяpman, suhbat skriptining o'zini sizning qaroringizni kutib qayta yozmadim.

### 3d. Dars tuzilishi qarori

**[QAROR]** `mentor-sessions.md`dagi mavjud haftalik S1 (Boshlash) / S2 (Amaliyot) / S3 (Fikr-mulohaza + kengaytirish) ritmini saqlash — bu mentorlik ritmi freymvorki, muayyan kurs mazmuniga bog'liq emas, shuning uchun katalog almashinuvidan o'zgarishsiz omon qoladi.

**[QAROR]** Qisqa kurslar uchun yangi qoida: bir nechta yangi kurslar 1 soatdan kam video (Prompt Engineering 101 — 0.58soat, Loop Engineering — 0.75soat). Eski reja har bir kursga to'liq hafta ajratganidek qilish o'rniga, **jami ~1 soatgacha bo'lgan kurslarni bitta haftaga birlashtiring**, yoki qisqa kursga haftaning faqat bir qismini egallashga ruxsat bering (masalan, S1+S2) va bo'shagan sessiyani mentor belgilagan kengaytirish loyihasi uchun ishlating. Quyidagi ishlab chiqilgan misolga qarang — Prompt Engineering 101 o'zi bitta haftaga zaxira bilan qulay sig'adi.

### 3e. Rivojlanishni tezlashtirish uchun ko'nikmalar

Hali tayyorlanmagan — keyinga qoldirilgan. Yuqoridagi tuzilmaviy qarorlar tasdiqlangandan so'ng, keyingi sessiyada `course-details.md` + olingan dars mazmunini avtomatik ravishda mentorlik sessiyasi rejasiga aylantirish uchun Matt Pocock yondashuvi asosidagi `/teach` uslubidagi ko'nikma, shuningdek kelajakdagi sessiyalar o'qishi mo'ljallangan har qanday hujjat uchun `/writing-for-agents` ko'rib chiqilishi kerak.

## 4. Ishlab chiqilgan misol — bitta to'liq hafta (1-bosqich, 2-hafta: Prompt Engineering 101)

Mavjud haqiqiy dars mazmuni asosida tuzilgan (`AI Learning Path/1. Master AI, ML & Context Foundations/1. Prompt Engineering 101/`) — kursni o'tayotganingizda siz tomoningizdan qo'lda joylashtirilgan, skreyping emas, lekin bu haqiqiy kurs mazmuni va hozircha mavjud eng aniq misol, taglama emas.

**Kurs:** Prompt Engineering 101 — Associate darajasi, 1 modul, 8 dars/7 laboratoriya, 0.58soat video (amaliyot uchun 2–3x rejalashtiring = ~1.5–2soat jami, bitta haftaga qulay sig'adi).

| Sessiya | Rol | Mazmun | Faoliyat |
|---|---|---|---|
| **S1 — Boshlash** | Yetakchi | Laboratoriya sayohati (Introduction) + Detailing for Clarity + Persona Play | Kursning o'zining umumiy→aniq misollaridan foydalanib jonli namoyish (masalan, "Iqlim o'zgarishi haqida gapirib bering" → "Iqlim o'zgarishi so'nggi o'n yillikda Atlantika okeanidagi bo'ronlar chastotasiga qanday ta'sir qilmoqda?"). S2 uchun tayyorgarlik topshirig'i: har bir talaba o'z ishidan bitta haqiqiy so'rovning 3 versiyasini tayyorlaydi — umumiy, batafsil, persona asosida. |
| **S2 — Amaliyot** | Murabbiy | Ajratuvchilar (uch marta teskari qo'shtirnoq, uch marta qo'shtirnoq, XML teglari, kalit so'z ajratuvchilari) + Bosqichma-bosqich aniqlashtirish | Juftlik mashqi: S1 tayyorgarligidagi "chalkash" haqiqiy so'rovni olib, ajratuvchilar bilan qayta tuzish va aniq bosqichlarga bo'lish. Mentor aylanib yuradi, to'siqlarni bartaraf qiladi. |
| **S3 — Fikr-mulohaza + kengaytirish** | Ko'rib chiqish | Misollar orqali ko'rsatish (few-shot) + Chiqish uzunligini belgilash | **Kengaytirish topshirig'i:** barcha 5 texnikani birlashtirgan holda haqiqiy dasturlash vazifasi uchun bitta so'rov yozish (batafsillik + persona + ajratuvchilar + bosqichma-bosqichlik + chiqish uzunligi) — bu ularning o'z S1/S2 so'roviga to'g'ridan-to'g'ri asoslanadi. Standart mezon bo'yicha individual uy vazifasini ko'rib chiqish (bajarildi/tugallandi · sifat · yondashuvni tushuntira oldimi · bitta yaxshilash). Keyingi haftaga oldindan ko'rib chiqish. |

**Qo'shimcha uy vazifasi (eski rejadan o'tkazilgan, hali ham mos):** shaxsiy so'rov-namunasi kutubxonasini topshirish — har bir texnika uchun bitta ishlab chiqilgan misol, o'z sohasidan.

## 5. To'rtinchi bosqich

Tayyorlanmagan — 3a–3d tasdiqlanishiga bog'liq. Kontent yaratish, alohida ommaviy kontent bosqichi emas, tekshirish paytida talab bo'yicha olingan har qanday narsani qayta ishlatishi kerak (`tasks.md`dagi "avval lokal" tamoyiliga muvofiq).

## 6. O'quv markazi bilan ko'tarish uchun ochiq masalalar

1. Dastur davomiyligi: ko'proq amaliy nisbat bilan ~20 haftada saqlash, yoki ma'lum video soatlarining ~50% kamayishini hisobga olib ~14–16 haftaga qisqartirish kerakmi? (§3a)
2. Pullik obunalar — ham bulut, ham AI vositalari darajalari — hali javobsiz (`tasks.md` 1-savol), endi AIOps Docker/K8s bilan bog'liq vositalar savollarini qo'shgani sababli yanada dolzarb.
3. AIOps Learn-By-Doing asosiy o'quv dasturi bo'lishi kerakmi yoki ixtiyoriy qo'shimcha, uning bir nechta kurslari yig'ish vaqtida hali chiqarilmaganini hisobga olsak?
4. Qabul talablaridan JS/Node'ni olib tashlash va Docker talabini oshirish bo'yicha rozilik (§3c).

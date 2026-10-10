From: Lena Kowalski
To: Sean Murphy, Priya Nair
Subject: RE: RE: ERP sample / mapping effort
Date: Thu 9 Oct

Hi both,

Following up on the call. Having looked at the fixed-width ERP file in more detail, the pricing table has no key field, so I'm having to infer product IDs from position. That's fragile. If the vendor changes the layout between now and cutover we'll load garbage and may not notice. I'd like us to ask the vendor for a layout spec in writing — I can do that if someone gives me the contact. Also Dev (Acme analyst) is the only person who can sanity check pricing and he's out from 3 Nov, so we need him to review before then. Realistically that means by 31 Oct.

Separately, the test environment is back up as of this morning, thanks Priya. I've reloaded 20% of the sample. Full load tomorrow.

Lena

---
From: Sean Murphy
Date: Thu 9 Oct
Lena — good catches. I'll talk to Tom about the vendor contact. Can we make sure the pricing review is on Priya's plan too.

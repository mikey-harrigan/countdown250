// Hosted Groups Program — official public roster.
// This file is the single source of truth for the live roster shown on
// /hosted-group-tables. Keep counts updated as real people join via the
// Google Forms (master Sheet → reflect changes here weekly).
//
// Featured threshold: tables with 6+ confirmed members earn the "Featured
// Hosted Group" badge (public toast + personalized signage at the event).

export interface HostedTable {
  /** Display name shown on the public roster */
  name: string;
  /** Optional one-line theme/description shown under the name */
  description?: string;
  /** Confirmed member count (seed at launch, real signups added on top) */
  count: number;
}

/** A Hosted Group earns "Featured" status (public toast + personalized
 *  signage) at this many confirmed members or more. */
export const FEATURED_THRESHOLD = 6;

/** Live roster shown on /hosted-group-tables, ordered by display preference. */
// 2026-06-18: Mike added Movement Mortgage, Latin Fashion Awards –
// America 250 Celebration, and Sankeys. They're appended at the end
// with count: 0 — counts are no longer displayed on the page, so the
// numeric values are kept here only for the Featured-badge threshold.
export const hostedTables: HostedTable[] = [
  { name: "Technical Staffing Inc.",                    count: 8  },
  { name: "JMU Alumni",                                 count: 12 },
  { name: "Virginia Tech Alumni",                       count: 8  },
  { name: "Lansdowne Neighbors",                        count: 8  },
  { name: "Georgetown Alumni",                          count: 4  },
  { name: "Healthcare Professionals",                   count: 6  },
  { name: "H Tragle 50th Bday",                         count: 6  },
  { name: "Univ. of MD Alumni",                         count: 6  },
  { name: "Walter Family Reunion",                      count: 8  },
  { name: "Knuckle Dragger Cattle Co.",                 count: 2  },
  { name: "Movement Mortgage",                          count: 0  },
  { name: "Latin Fashion Awards – America 250 Celebration", count: 0 },
  { name: "Sankeys",                                    count: 0  },
];

/** Convenience: derived flat list of names, kept for any legacy imports. */
export const allHostedGroups = hostedTables.map((t) => t.name);

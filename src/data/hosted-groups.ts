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
export const hostedTables: HostedTable[] = [
  { name: "Technical Staffing Inc.",       count: 8  },
  { name: "JMU Alumni",                    count: 12 },
  { name: "Virginia Tech Alumni",          count: 8  },
  { name: "Lansdowne Neighbors",           count: 8  },
  { name: "Georgetown Alumni",             count: 4  },
  { name: "Healthcare Professionals",      count: 6  },
  { name: "H Tragle 50th Bday",            count: 6  },
  { name: "Univ. of MD Alumni",            count: 6  },
  { name: "Walter Family Reunion",         count: 8  },
];

/** Convenience: derived flat list of names, kept for any legacy imports. */
export const allHostedGroups = hostedTables.map((t) => t.name);

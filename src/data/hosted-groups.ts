// Hosted Group Tables — official public list.
// This file is the single source of truth for group names shown on the website.
// Keep identical to the Eventbrite dropdown; when adding/approving/renaming a group,
// update BOTH this file AND the Eventbrite checkout dropdown.
//
// To add a group: add its exact name to the appropriate category below.
// To rename: change the string here AND update Eventbrite to match exactly.
// To remove: delete the string here AND remove from Eventbrite.

export interface HostedGroupCategory {
  /** Section heading shown on the Hosted Group Tables page */
  name: string;
  /** Group names — case and punctuation must match Eventbrite exactly */
  groups: string[];
}

export const hostedGroupCategories: HostedGroupCategory[] = [
  {
    name: "Alumni & Schools",
    groups: [
      "JMU Alumni",
      "Virginia Tech Alumni",
      "UVA Alumni",
      "GMU Alumni",
    ],
  },
  {
    name: "Neighborhoods & Local",
    groups: [
      "Lansdowne Neighbors",
      "Loudoun Professionals",
    ],
  },
  {
    name: "Industry & Networking",
    groups: [
      "Real Estate Professionals",
      "Mortgage Professionals",
      "Government Affairs",
      "Tech Leaders",
    ],
  },
  {
    name: "Interests & Social",
    groups: [
      "Golf Enthusiasts",
      "DC Sports Fanatics",
    ],
  },
];

/** Flat list of all group names, useful for quick display or validation. */
export const allHostedGroups = hostedGroupCategories.flatMap((c) => c.groups);

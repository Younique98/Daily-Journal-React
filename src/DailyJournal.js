import React from "react";
import { EntryProvider } from "./components/EntryProvider";
import { EntryForm } from "./components/EntryForm";
import { EntryList } from "./components/EntryList";
import { MoodProvider } from "./components/mood/MoodProvider";
import { TagProvider } from "./components/tag/TagProvider";

export const DailyJournal = () => {
  return (
    <div className="DailyJournal">
      <EntryProvider>
        <MoodProvider >
          <TagProvider>
          <EntryForm />
          <EntryList />
          </TagProvider>
        </MoodProvider>
      </EntryProvider>
    </div>
  );
};

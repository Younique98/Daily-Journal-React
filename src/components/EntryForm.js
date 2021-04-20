import React, { useContext, useState, useEffect } from "react"
import { EntryContext } from "./EntryProvider"
import { MoodContext } from "./mood/MoodProvider"
import { TagContext } from "./tag/TagProvider"


export const EntryForm = (props) => {
    
    const { addEntry, updateEntry, entry, setEntry } = useContext(EntryContext)
    
    const { moods, getMoods } = useContext(MoodContext);
    const { tags, getTags } = useContext(TagContext);
    const [tagSelected, setTagSelected ] = useState("");
    const [editMode, editModeChanged] = useState(false);

    useEffect(() => {
        getMoods()
        .then(getTags)
    }, [])


    useEffect(() => {
        if ('id' in entry) {
            editModeChanged(true)
        }
        else {
            editModeChanged(false)
        }
    }, [entry])

    const handleControlledInputChange = (event) => {
        /*
            When changing a state object or array, always create a new one
            and change state instead of modifying current one
        */
        const newEntry = Object.assign({}, entry)
        newEntry[event.target.name] = event.target.value
        setEntry(newEntry)
    }



    const constructNewEntry = () => {

        if (editMode) {
            updateEntry({
                id: entry.id,
                concept: entry.concept,
                entry: entry.entry,
                date: entry.date,
                moodId: parseInt(entry.moodId)
            })
        } else {
            addEntry({
                concept: entry.concept,
                entry: entry.entry,
                date: Date.now(),
                moodId: parseInt(entry.moodId)
            })
        }
        setEntry({ concept: "", entry: "", moodId: 0 })
    }

    return (
        <form className="EntryForm">
            <h2 className="EntryForm__title">{editMode ? "Update Entry" : "Create Entry"}</h2>
            <fieldset>
                <div className="form-group">
                    <label htmlFor="concept">Todays Journal Concept: </label>
                    <input type="text" name="concept" required autoFocus className="form-control"
                        proptype="varchar"
                        placeholder="Concept"
                        value={entry.concept}
                        onChange={handleControlledInputChange}
                    />
                </div>
            </fieldset>
            <fieldset>
                <div className="form-group">
                    <label htmlFor="entry">Enter Your THoughts - Today's Entry: </label>
                    <input type="text" name="entry" required className="form-control"
                        proptype="varchar"
                        placeholder="Entry"
                        value={entry.entry}
                        onChange={handleControlledInputChange}
                    />
                </div>
            </fieldset>
            <fieldset>
                <div className="form-group">
                    <label htmlFor="moodId">Select Your Mood: </label>
                    <select name="moodId" className="form-control"
                        proptype="int"
                        value={entry.moodId}
                        onChange={handleControlledInputChange}>

                        <option value="0">Select a mood</option>
                        {moods.map(m => (
                            <option key={m.id} value={m.id}>
                                {m.label}
                            </option>
                        ))}
                        
                    </select>
                    
                </div>
            </fieldset>
            {
        tags.map(tag => {
          return <>
          <label>Please Select a Tag:</label>
            <input type="radio" value={tag.id} name="tag_id"
              onChange={handleControlledInputChange}
            /> {tag.name}
          </>
        })
      }
         <div>
                <button type="submit"
                onClick={evt => {
                    evt.preventDefault()
                    constructNewEntry()
                }}
                className="btn btn-primary">
                {editMode ? "Update" : "Save"}
            </button>
            </div>
        </form>
    )
}
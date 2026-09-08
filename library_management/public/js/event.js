
frappe.realtime.on("play_save_sound", (data)=>{
    console.log("play_save_sound event received", data);
    frappe.utils.play_sound("ping")
})
console.log("Event JS loaded");
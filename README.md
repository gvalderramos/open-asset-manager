# Open Asset Manager

This library ofter an API to control assets and files in your server.

In the creative world (VFX, film, game companies, or advertisement studios), each asset is compound by many files - Images, textures, DCC files (Maya, Houdini, Nuke), etc.

These assets usually have a lot of project dependencies so this makes reuse difficult in other projects. 

That is the main reason for this library - Make it easier the creation of studio assets library and provide a way to reuse the same files in any project you want to, independently of the project manager your studio is using (Shotgrid, Ftrack).

This project is an open-source aimed. All vendor libraries are open-source and, everyone is welcome to contribute. For more information, reach out to us.

    Warning: This library is in WIP and doesn't have a runnable version yet.

---
### Dependencies

This library use the MongoDb to store the asset information. There is a docker-compose already configured to do it. So to run this service you just need to run the following command:

```bash
cd ./open-asset-manager

sudo docker-compose up
```
